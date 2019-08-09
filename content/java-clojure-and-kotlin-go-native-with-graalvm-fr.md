Title: Du code Java/Kotlin/Clojure "natif" grâce à GraalVM
Date: 2019-08-09 07:00
Tags: java clojure kotlin native graalvm jvm
Slug: java-clojure-and-kotlin-go-native-with-graalvm
Author: Nicolas Kosinski
Summary: Générer des exécutables natifs via GraalVM pour des outils en ligne de commande implémentés en Java, Kotlin ou Clojure
Status: draft
Lang: fr

[Audience présumée](https://v4.chriskrycho.com/2018/assumed-audiences.html) : développeurs.euses intéressés.ées par l'écosystème Java et plus particulièrement sur l'amélioration des performances et la génération d'exécutables.

Plan :

1. Introduction
2. Outils utilisés
3. Exécutable optimisé pour une application "WordCount" `Java`
4. Exécutable optimisé pour une application `Kotlin`
5. Exécutable moins optimisé pour une application `Clojure`
6. Conclusion



## Introduction

Suite à mes premiers essais infructueux l'an dernier (lire mon article précédent [Du Clojure "natif" grâce à GraalVM](https://nicokosi.github.io/clojure-goes-native-with-graalvm.html)), voici un compte rendu plus positif de mes expérimentations avec les versions _release_ de [GraalVM](https://www.graalvm.org/) sorties à partir de mai 2019 (cf. les [_release notes_](https://www.graalvm.org/docs/release-notes/)).

## Outillage

Nous utiliserons les outils suivants :

- [GraalVM Community Edition](https://www.graalvm.org/downloads/) ("_a High-performance polyglot VM_") pour générer des exécutables à partir de bytecode JVM
- [SDKMAN!](https://sdkman.io/) ("_The Software Development Kit Manager_") pour installer / utiliser des versions différentes du _Java Development Kit_ / _Java Runtime Environment_
- [time](http://manpages.ubuntu.com/manpages/cosmic/en/man1/time.1.html) ("_run programs and summarize system resource usage_") pour mesurer le temps d'exécution
- [valgrind](http://valgrind.org/) ("_tool for memory debugging, memory leak detection, and profiling_") pour évaluer l'empreinte mémoire des processus

## Exécutable optimisé pour une application "WordCount" `Java`

Notre "hello world" est un programme Java de 10 lignes qui compte le nombre de mots d'un fichier de texte : [wordcount-with-java-stream](https://github.com/nicokosi/wordcount-with-java-stream).

Générons un JAR exécutable via Maven et OpenJDK, cela prend 2 secondes sur ma machine ⚡ :

```sh
$ sdk use java 8.0.222.hs-adpt
Using java version 8.0.222.hs-adpt in this shell.
$ time ./mvnw clean --quiet compile
./mvnw clean --quiet compile  6.24s user 0.31s system 323% cpu 2.022 total
```

Puis générons l'exécutable via GraalVM native-image, cela prendre 40 secondes sur ma machine 🐌 :

```sh
$ time $HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image \
     --enable-https \
     --no-fallback \
     --no-server \
     -cp target/classes org.nicokosi.WordCount \
     wordcount-with-java-stream
$HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image --enable-https   -c  236,70s user 2,75s system 566% cpu 42,285 total
```

Comparons les temps d'exécution pour un petit fichier d'entrée :

```sh
$ alias wordcount_java=" $HOME/.sdkman/candidates/java/8.0.222.hs-adpt/bin/java -cp target/classes org.nicokosi.WordCount"
$ time wordcount_java /etc/hosts
File /etc/hosts contains 26 words
/home/nkosinski/.sdkman/candidates/java/8.0.222.hs-adpt/bin/java -cp     0,16s user 0,02s system 152% cpu 0,118 total
```

```sh
$ time ./wordcount-with-java-stream /etc/hosts
File /etc/hosts contains 26 words
./wordcount-with-java-stream /etc/hosts  0,00s user 0,01s system 92% cpu 0,007 total
```

Puis comparons l'empreinte mémoire :

```sh
$ JAVA_HOME=$HOME/.sdkman/candidates/java/8.0.222.hs-adpt \
  valgrind java -cp target/classes org.nicokosi.WordCount /etc/hosts

==23352== HEAP SUMMARY:
==23352==     in use at exit: 34,892,297 bytes in 6,155 blocks
==23352==   total heap usage: 14,555 allocs, 8,400 frees, 49,960,719 bytes allocated  **
```

```sh
$ valgrind ./wordcount-with-java-stream /etc/hosts

==23753== HEAP SUMMARY:
==23753==     in use at exit: 10,468 bytes in 3 blocks
==23753==   total heap usage: 8 allocs, 5 frees, 12,436 bytes allocated**
```

Pour résumer, au prix d'un temps de compilation plus long (40 secondes au lieu de 2 secondes), GraalVM :

- accélère l'exécution "courte" (7 millisecondes au lieu de 118 millisecondes)
- réduit l'empreinte mémoire de notre application (10 kilooctets au lieu de 34 mégaoctets)

## Exécutable optimisé pour une application `Kotlin`

Faisant la même chose pour une application [`Kotlin`](https://kotlinlang.org/) un peu plus complexe, [pullpitoK](https://github.com/nicokosi/pullpitoK/) (200 lignes de codes avec des librairies tierces) qui consomme les API GitHub pour afficher des statistiques sur les pull requests GitHub.

La phase de constuction étant similaire au paragraphe précédent, concentrons-nous sur la comparaison du temps de démarrage pour une exécution rapide (affichage de l'aide souvent appellée "usage message"](https://en.wikipedia.org/wiki/Usage_message)) :

```sh
$ export PATH=$HOME/.sdkman/candidates/java/8.0.222.hs-adpt/bin:$PATH
$ time (java -jar ./build/libs/pullpitoK-all.jar | head -1)
Usage: pullpitoK <repository> <token>
( java -jar ./build/libs/pullpitoK-all.jar | head -1; )  0.08s user 0.02s system 108% cpu 0.093 total
```

```sh
$ alias pullpitoK="PULLPITOK_LIBSUNEC=$HOME/.sdkman/candidates/java/19.1.1-grl/jre/lib ./pullpitoK"
$ time (pullpitoK --help | head -1)
Usage: pullpitoK <repository> <token>
( PULLPITOK_LIBSUNEC=/Users/nicolas/.sdkman/candidates/java/19.1.1-grl/jre/li)  0.00s user 0.00s system 88% cpu 0.009 total
```

Soit 10 millisecondes avec la version native contre 100 millisecondes pour la version JVM.

Comparons maintenant l'empreinte mémoire :

```sh
$ valgrind java -jar ./build/libs/pullpitoK-all.jar
...
Usage: pullpitoK <repository> <token>
...
==26273== HEAP SUMMARY:
==26273==     in use at exit: 32,181,758 bytes in 2,134 blocks
==26273==   total heap usage: 5,725 allocs, 3,591 frees, 33,187,784 bytes allocated
...
```

```sh
$ valgrind pullpitoK | head -1
...
Usage: pullpitoK <repository> <token>
...
==27690== HEAP SUMMARY:
==27690==     in use at exit: 228 bytes in 1 blocks
==27690==   total heap usage: 6 allocs, 5 frees, 2,196 bytes allocated
```

Soit 12 kilooctets avec la version native contre 32 mégaoctets pour la version JVM.

## Exécutable _moins optimisé_ pour une application `Clojure`

Dans mon billet [Du Clojure "natif" grâce à GraalVM](https://nicokosi.github.io/clojure-goes-native-with-graalvm.html), je me suis heurté à deux problèmes :

- GraalVM était encore expérimental (_release candidates_) à l'époque
- l'outil Native Image possède des [limitations](https://github.com/oracle/graal/blob/master/substratevm/LIMITATIONS.md) qui concernent notamment le chargement de classes dynamiques, l'utilisation de la réflexion (API java.lang.reflect) etc.

Essayons de refaire l'essai avec une version _release_ de GraalVM pour l'application [hubstats](https://github.com/nicokosi/hubstats/) (200 lignes de codes, utilisation de librairies tierces pour appeller les API HTTP GitHub).

```sh
$ time $HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image \
   --enable-https \
   --no-fallback \
   --no-server \
   -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar \
   hubstats
```

La compilation native échoue 💥. Voici un extrait du message d'erreur :

```
Error: Unsupported features in 4 methods
Detailed message:
Error: Unsupported type java.lang.invoke.MemberName is reachable: All methods from java.lang.invoke should have been replaced during image building.
To diagnose the issue, you can add the option --report-unsupported-elements-at-runtime. The unsupported element is then reported at run time when it is accessed the first time.
...
```

Nous pourrions corriger ça en adaptant le code source. Par facilité, essayons le mode `fallback` ("solution de repli") de Native Image qui permet de contourner les limitations en embarquant une JVM classique :

```sh
$ # Contruction de l'exécutable avec GraalVM
time $HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image \
   --enable-https \
   --force-fallback \
   --no-server \
   -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar \
   hubstats
...
[hubstats:31661]      [total]:  14,663.95 ms
Warning: Image 'hubstats' is a fallback image that requires a JDK for execution (use --no-fallback to suppress fallback image generation).
$HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image --enable-https       78,73s user 1,31s system 536% cpu 14,926 total
```

Etant donné que le mode fallback est utilisé, les temps de démarrage sont maintenant similaires :

```sh
$ export PATH=$HOME/.sdkman/candidates/java/8.0.222.hs-adpt/bin:$PATH
$ time (java -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar | head -1)
Display statistics for GitHub pull requests.
( java -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar | head -1; )  3,36s user 0,10s system 262% cpu 1,318 total
```

```sh
$ time (./hubstats | head -1)

Display statistics for GitHub pull requests.
( ./hubstats | head -1; )  2,86s user 0,14s system 236% cpu 1,272 total

```

mais l'empreinte mémoire est énormément réduite :

```sh
$ export PATH=$HOME/.sdkman/candidates/java/8.0.222.hs-adpt/bin:$PATH
$ valgrind java -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar
...
Display statistics for GitHub pull requests.
...
==2690== HEAP SUMMARY:
==2690==     in use at exit: 38,656,326 bytes in 34,800 blocks
==2690==   total heap usage: 170,569 allocs, 135,769 frees, 406,386,571 bytes allocated
...
```

```sh
$ valgrind pullpitoK
...
Usage: pullpitoK <repository> <token>
...
==5747== HEAP SUMMARY:
==5747==     in use at exit: 228 bytes in 1 blocks
==5747==   total heap usage: 6 allocs, 5 frees, 2,196 bytes allocated
...
```

## Conclusion

Au travers de ces trois petites applications utilisant des langages différents (`Java`, `Kotlin`, `Clojure`), nous avons pu vérifier le double intérêt des images natives : avoir un **exécutable compact** déployable sans Java Virtual Machine et bénéficier d'une **consommation mémoire réduite** et (parfois !) d'un **démarrage rapide**.

De plus, on présent l'intérêt qu'aura GraalVM pour moderniser Java, en particulier pour un usage en **_cloud-computing_** et pour les **microservices**. Se référerer aux frameworks tels [Quarkus](https://quarkus.io/) et [Micronaut](https://micronaut.io/). 

A  tester ultérieurement :

- la gestion de la mémoire par le ramasse-miettes (_garbage collector_)
- la différence entre la version gratuite et les versions _Community Edition_ et _Enterprise Edition_.