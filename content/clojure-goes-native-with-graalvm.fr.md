+++
title = "Du Clojure \"natif\" grâce à GraalVM"
description = "Générer un programme exécutable natif via GraalVM pour un projet Clojure, 'hubstats'."
date = 2018-05-12
[taxonomies]
tags = ["clojure", "native", "graalvm"]
+++
# Du Clojure "natif" grâce à GraalVM

## GraalVM, qu'est-ce que c'est ?

[GraalVM](http://www.graalvm.org/) est une machine virtuelle multi-langages : Java, autres langages de la machine virtuelle Java (Scala, Groovy, Kotlin etc.), JavaScript, LLVM, Ruby et R.

GraalVM permet également de générer des exécutables natifs à partir du code Java :
```
For JVM-based languages, GraalVM offers a mechanism to create precompiled native images with instant start up and low memory footprint.
```

Oracle labs a annoncé en avril 2018 la sortie de [GraalVM 1.0 release candidate](https://blogs.oracle.com/developers/announcing-graalvm), donc c'est parti pour un essai !


## Construire un exécutable à partir d'un projet Clojure

[hubstats](https://github.com/nicokosi/hubstats) est mon projet perso implémenté en Clojure qui permet d'afficher des statistiques sur les pull requests GitHub. C'est un outil en ligne de commande utilisant une machine virtuelle Java, donc GraalVM devrait permettre d'accélérer son démarrage en générant un exécutable "natif".

Notes :

- Cet [article intéressant](https://www.innoq.com/en/blog/native-clojure-and-graalvm/
) m'a inspiré et m'a aidé.

- J'ai utilisé la version "Community Edition" de GraalVM qui est gratuite et open source (une version "Enterprise Edition" existe également).

### Essai n°1

A partir du "fat" JAR de mon projet 'hubstats' ("fat jar" : archive de code Java qui inclut toutes les dépendances), j'ai lancé la commande `native-image` de [GraaVM 1.0.0-rc1 dans un conteneur Docker](https://github.com/Danny02/graalvm-docker) :

```sh
native-image \
  -jar hubstats-0.1.0-SNAPSHOT-standalone.jar \
  -H:+ReportUnsupportedElementsAtRuntime \
  hubstats.core
```
(cf. [tous les détails](https://github.com/nicokosi/hubstats/pull/12/files))

Pas de chance, la génération de l'exécutable échoue :
```
Step 4/15 : RUN native-image   -jar hubstats-0.1.0-SNAPSHOT-standalone.jar   -H:+ReportUnsupportedElementsAtRuntime   hubstats.core
 ---> Running in e7f911774bd4
Build on Server(pid: 11, port: 26681)*
   classlist:   3,159.26 ms
       (cap):   1,485.02 ms
       setup:   2,563.80 ms
    analysis:  10,109.06 ms
fatal error: java.lang.NullPointerException
	at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
	at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
	at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
	at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
	at java.util.concurrent.ForkJoinTask.getThrowableException(ForkJoinTask.java:598)
	at java.util.concurrent.ForkJoinTask.get(ForkJoinTask.java:1005)
	at com.oracle.svm.hosted.NativeImageGenerator.run(NativeImageGenerator.java:398)
	at com.oracle.svm.hosted.NativeImageGeneratorRunner.buildImage(NativeImageGeneratorRunner.java:240)
	at com.oracle.svm.hosted.NativeImageGeneratorRunner.build(NativeImageGeneratorRunner.java:337)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.executeCompilation(NativeImageBuildServer.java:378)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.lambda$processCommand$8(NativeImageBuildServer.java:315)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.withJVMContext(NativeImageBuildServer.java:396)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.processCommand(NativeImageBuildServer.java:312)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.processRequest(NativeImageBuildServer.java:256)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.lambda$serve$7(NativeImageBuildServer.java:216)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	at java.lang.Thread.run(Thread.java:748)
Caused by: java.lang.NullPointerException
	at com.oracle.graal.pointsto.ObjectScanner.scanField(ObjectScanner.java:113)
	at com.oracle.graal.pointsto.ObjectScanner.doScan(ObjectScanner.java:263)
	at com.oracle.graal.pointsto.ObjectScanner.finish(ObjectScanner.java:307)
	at com.oracle.graal.pointsto.ObjectScanner.scanBootImageHeapRoots(ObjectScanner.java:78)
	at com.oracle.graal.pointsto.ObjectScanner.scanBootImageHeapRoots(ObjectScanner.java:60)
	at com.oracle.graal.pointsto.BigBang.checkObjectGraph(BigBang.java:581)
	at com.oracle.graal.pointsto.BigBang.finish(BigBang.java:552)
	at com.oracle.svm.hosted.NativeImageGenerator.doRun(NativeImageGenerator.java:653)
	at com.oracle.svm.hosted.NativeImageGenerator.lambda$run$0(NativeImageGenerator.java:381)
	at java.util.concurrent.ForkJoinTask$AdaptedRunnableAction.exec(ForkJoinTask.java:1386)
	at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:289)
	at java.util.concurrent.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1056)
	at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1692)
	at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:157)
Error: Processing image build request failed
```
Le problème ressemble fortement à [issue#385](https://github.com/oracle/graal/issues/385) et [issue#375](https://github.com/oracle/graal/issues/375). Si je comprends bien, il est lié à l'une des limitations de GraalVM : ["static initializers" limitation](https://github.com/oracle/graal/blob/master/substratevm/LIMITATIONS.md#static-initializers). 😢


### Essai n°2

Puisque certaines corrections étaient uniquement disponibles dans le [code source de GraalVM](https://github.com/graalvm/), j'ai voulu essayer avec le module `substratevm`
(qui inclut la commande 'native-image') construit à partir du code source.


J'ai donc récupéré le code source de GraalVM :
```sh
git clone git@github.com:oracle/graal.git
```
Puis en suivant les [indications du module substratevm](https://github.com/oracle/graal/tree/master/substratevm), j'ai téléchargé le [JDK GraalVM "labs"](http://www.oracle.com/technetwork/oracle-labs/program-languages/downloads/index.html) puis j'ai construit le module 'substratevm' :
```sh
cd substratevm
JAVA_HOME=~/Downloads/labsjdk1.8.0_161-jvmci-0.42/Contents/Home ../../mx/mx build
```

J'ai ensuite lancé la commande 'native-image' qui est malheuresement restée "coincée" :
```
$> JAVA_HOME=~/Downloads/labsjdk1.8.0_161-jvmci-0.42/Contents/Home ../graal/substratevm/native-image -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar hubstats.core
Build on Server(pid: 18933, port: 55103)*
   classlist:   2,744.32 ms
       (cap):   1,531.16 ms
       setup:   2,401.40 ms
```

Une anomalie similaire à déjà été rapportée : ["native image failed to build jar](https://github.com/oracle/graal/issues/411). 😭


### Conclusion

C'est sûr, ces premiers essais ont été infructueux. GraalVM est un projet encore jeune que je ne connais pas vraiment. Néanmoins, ce fut une expérience sympathique de découvrir cet outil prometteur ! 😍

A refaire sous peu, avec un nouvel article à la clé ?
