Title: Re-découvrons le langage Go avec "pullpigo", un petit projet d'expérimentation
Date: 2019-12-24 07:00
Tags: golang native
Slug: rediscovering-Golang-with-pullpigo
Author: Nicolas Kosinski
Summary: (Re)découvrir le langage de programmation Go avec un petit outil en ligne de commande, "pullpigo"
Lang: fr

# Re-découvrons le langage Go avec "pullpigo", un petit projet d'expérimentation

Développant au quotidien en Java, j'avais envie d'apprendre quelques rudiments du langage de programmation __[Go](https://golang.org/)__.
Pour ce faire, j'ai implémenté un petit outil en __ligne de commande (_CLI_)__ afin d'afficher des informations sur les pull requests GitHub.
J'ai créé ainsi un petit projet, versionné dans GitHub, [pullpigo](https://github.com/nicokosi/pullpigo). Son but 
est d'afficher le nombre d'événements du type "tant d'événements créés par tel auteur GitHub (_commiter_)" en utilisant une API publique de GitHub.

Notez que j'ai déjà implémenter un outil similaire dans d'autres langages (que je voulais aussi découvrir ou approfondir) : en __Clojure__ (cf. [hubstats](https://github.com/nicokosi/hubstats)), __Kotlin__ (cf. [pullpitoK](https://github.com/nicokosi/pullpitoK)) et __Rust__ (cf. [pullpito](https://github.com/nicokosi/pullpito)).

## Les exécutables natifs sont rapides 🚀

Compilons pullpigo :

```shell
$ go clean
$ time go build
go build  1.05s user 0.58s system 105% cpu 1.559 total
```
Puis lançons le :
```shell
time ./pullpigo -repo=vidal-community/atom-jaxb
GitHub repository 'vidal-community/atom-jaxb'
  2 events created by amairi
  1 events created by fchetouani
  6 events created by AElMehdiVidal
  3 events created by jcgay
./pullpigo -repo=vidal-community/atom-jaxb  0.07s user 0.03s system 20% cpu 0.482 total
```

Comparons ces temps avec ceux d'un projet similaire implémenté en Kotlin, ([pullpitoK](https://github.com/nicokosi/pullpitoK/)) :
```shell
$ ./gradlew clean
$ time ./gradlew build --quiet
./gradlew build --quiet  1.37s user 0.17s system 39% cpu 3.932 total
$ time ./gradlew run --quiet --args "vidal-community/atom-jaxb"

pull requests for "vidal-community/atom-jaxb" ->
            opened per author
                amairi: 1
            commented per author
                AElMehdiVidal: 1
                jcgay: 1
            closed per author

./gradlew run --quiet --args "vidal-community/atom-jaxb"  1.37s user 0.18s system 62% cpu 2.473 total
```
Compilation rapide + exécution rapide = ❤️

## Les librairies et l'outillage standards de Go sont complets 📦

Pour appeler l'[API REST v3 'events' de GitHub](https://developer.github.com/v3/activity/events/), j'avais besoin de : un client HTTP, un _parser_ JSON ainsi qu'un _framework_ de test. C'est cool, tout est présent dans les librairies de base : [testing](https://golang.org/pkg/testing/), [HTTP client](https://golang.org/pkg/net/http/) et [JSON parsing](https://golang.org/pkg/encoding/json/).

J'ai donc pu implémenter mon outil sans utiliser une seule librairie tierce !

J'ai également apprécié l'outillage (notez mon _background_ Java) :

- pour __formatter le code__, il sufffit de lancer la commande `go fmt`, sans aucune configuration.

- pour analyser statiquement son code, un __code linter__ est également inclus. Il suffit d'installer [https://github.com/golang/linttype]([golang/linttype) et de lancer la commande `golint`, sans configuration (pour être franc, ce _linter_ ne m'a pas aidé pour coder pullpigo mais je trouve ça génial que cet outil existe).

## Opportunités "annexes" 😎

En dehors du langage et des libraries, ce petit projet a aussi été l'occasion d'**essayer et d'apprendre de nouveaux outils**. En l’occurrence :

- [Visual Studio Code](https://code.visualstudio.com/), un environnement de développement (_Integrated Development Environment_) que je n'utilise pas professionnellement.

- [GitHub Actions](https://github.com/features/actions), une plate-forme pour l'intégration continue : chaque commit git GitHub déclenche la compilation et les tests unitaires. Bien que je n'avais jamaais utilisé GitHub Actions, ça a été rapide à mettre en place (quelques minutes). En en plus, c'est gratuit ! 

Un autre point bonus, j'ai apprécié de **discuter et d'échanger** avec des gens que je connais (et pas uniquement de "googler").

Dans mon cas, mes "amis Golang" ont été :

- [Jean-Christophe](https://github.com/jcgay/) qui m'a motivé et m'a aidé à corriger un problème de _parsing_ JSON. 😅

- [Florent](https://github.com/fbiville) qui m'a donné des pointeurs sympas vers des librairies : [testing/quick](https://golang.org/pkg/testing/quick/) pour le _property-based testing_, [ginkgo](https://github.com/onsi/ginkgo) pour les test style _BDD_ et [gomega](https://github.com/onsi/gomega) pour les assertions de test. A essayer ! 😎

### La suite ? 🔮

Quelques pistes :

- Améliorer les messages en sortie. Par exemple, afficher les compteurs par type d'événements ("pull requests créés", "pull requests fusionnées" etc.)

- Récupérer les données de l'API `GraphQL` de GitHub ([GitHub's GraphQL API v4](https://developer.github.com/v4/)) de façon à ne pas être limité aux 300 derniers événements (c'est une limitation de l'API GitHub REST).

- Utiliser des dépendances pour les tests (assertions plus faciles, property-based testing etc.) et en profiter pour découvrir la gestion des dépendances en Go.

A suivre !