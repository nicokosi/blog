Title: Du Kotlin et du Clojure "natif" grâce à GraalVM
Date: 2019-07-12 07:00
Tags: clojure kotlin native graalvm
Slug: clojure-and-kotlin-go-native-with-graalvm
Author: Nicolas Kosinski
Summary: Générer des exécutables natifs via GraalVM pour des outils en ligne de commande implémentés en Kotlin et en Clojure 
Status: draft
Lang: fr

## Intro

Suite à mes premiers essais infructueux l'an dernier (lire mon article précédent [Du Clojure "natif" grâce à GraalVM](https://nicokosi.github.io/clojure-goes-native-with-graalvm.html)), voici un compte rendu plus positif de mes expérimentations avec 
les versions "release" de GraalVM sorties à partir de mai 2019 (cf. la [_release note 19.0.0_](https://github.com/oracle/graal/releases/tag/vm-19.0.0)).

## Un exécutable à partir d'une application Kotlin, `pullpitoK`

J'ai eu envie de tester GraalVM à partir d'un langage statique, plus proche de Java que Clojure. J'ai donc développé [pullpitoK](https://github.com/nicokosi/pullpitoK/), qui est un portage de [hubstats](https://github.com/nicokosi/hubstats) en [`Kotlin`](https://kotlinlang.org/).

### Génération de l'exécutable
**à compléter**

### Exécutable vs JAR

#### Temps de démarrage
**à compléter**

#### Empreinte mémoire
**à compléter**

## Un exécutable à partir d'une application Clojure, `hubstats`
**à compléter**
Expliquer le mode `fallback` lié aux limitations.

### Exécutable vs JAR
#### Temps de démarrage
**à compléter**

#### Empreinte mémoire
**à compléter**

## Conclusion
**à compléter**