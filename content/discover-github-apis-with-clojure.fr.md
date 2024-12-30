+++
title = "A la découverte des API GitHub en apprenant Clojure"
description = "A la découverte des API GitHub en apprenant Clojure."
date = 2017-01-11
update = 2024-12-30
[taxonomies]
tags = ["clojure", "github"]
+++
# A la découverte des API GitHub en apprenant Clojure

Il est toujours intéressant d'apprendre quelque chose, même si ça ne concerne pas directement le travail quotidien. Pour citer [The Pragmatic Programmer](https://pragprog.com/book/tpp/the-pragmatic-programmer) (note pour moi-même : relire ce livre 🤓) :
> Invest Regularly in Your Knowledge Portfolio


Mon dernier projet personnel "pour apprendre" a été de créer un outil en ligne de commande, nommé [hubstats](https://github.com/nicokosi/hubstats), permettant d'afficher un résumé statistique concernant les [pull requests GitHub](https://help.github.com/articles/github-glossary/#pull-request), afin d'avoir quelques métriques sur leur utilisation par mon équipe, au travail.

Ce modeste projet m'a permis de mettre en pratique le langage de programmation [Clojure](https://clojure.org/) (que je connaissais un tout petit peu), mais aussi de découvrir les [API REST](https://developer.github.com/v3/) et [GraphQL](https://docs.github.com/en/graphql) de GitHub.

J'ai en plus eu la chance d'échanger régulièrement avec un collègue connaissant bien Clojure. Ce fut appréciable et motivant, merci Jérôme aka [@jprudent](https://github.com/jprudent) !

<br/>
## A quoi ça sert, _hubstats_ ?

_hubstats_ est un outil en ligne de commandes qui permet de connaître, pour un [repository GitHub](https://help.github.com/articles/github-glossary/#repository) donné, le nombre de pull requests ouvertes / commentées / mergées par auteur sur une période donnée (dernière semaine, deux dernières semaines, depuis une date donnée etc.).

Voici un exemple de rapport fourni par _hubstats_ :
```bash
lein run --organization softwarevidal --repository arthur --token $token
pull requests for softwarevidal/arthur ->
    since 1 week(s):
        9 opened / 56 commented / 5 closed
        opened per author: {"cmahalin" 5, "jcgay" 2, "AElMehdiVidal" 2}
        commented per author: {"vidal-rm" 30, "jcgay" 17, "cmahalin" 9}
        closed per author: {"cmahalin" 2, "AElMehdiVidal" 2, "jprudent" 1}
```

<br/>
## Comment ça marche ?

J'ai choisi d'utiliser Clojure, un langage très différent de Java que j'utilise au quotidien.
Les particularités suivantes ont notamment retenu mon attention :

* développement dynamique et interactif : code plus simple, notamment pour un petit outil "interne" ; le [REPL](https://clojure.org/about/dynamic#_the_repl) est un outil de base et son utilisation est particulièrement adaptée pour un projet de "découverte"
* programmation fonctionnelle : l'approche fonctionnelle, bien qu'encouragée dans les langages "mainstream" tel Java, est obligatoire en Clojure. Les fonctions sont reines ("_first-class citizen_"), l'immutabilité et la récursivité sont de mise.
* Lisp : Clojure étant un Lisp, le code s'écrit un peu différemment : il s'apparente à de la donnée et peut se transformer facilement via des commandes de type [paredit](https://www.emacswiki.org/emacs/ParEdit).
* simplicité : Clojure est un langage simple dont la philosophie est d'utiliser des petites librairies plutôt que des gros frameworks.

Se référer à [Clojure Rationale](https://clojure.org/about/rationale) pour plus d'informations sur les apports de Clojure.


Mon environnement de développement a été :

- [IntelliJ IDEA](https://www.jetbrains.com/idea/) avec le [plugin Cursive](https://cursive-ide.com/)
- [mode _paredit_ de Cursive](https://cursive-ide.com/userguide/paredit.html)
- [Leiningen](https://leiningen.org/) comme outil de build
- [Travis CI](https://travis-ci.org/) pour l'intégration continue


<br/>
## Et alors ?

Ce que j'ai aimé :

* cet aparté qui m'a changé de mes "habitudes en Java"
* l'utilisation de _paredit_ pour manipuler son code (créer, déplacer ou supprimer du code) est un peu déroutante au début mais très plaisante ensuite
* l'utilisation du REPL qui m'a servi :
    * de "brouillon" pour écrire mon code
    * pour diagnostiquer et corriger des bug
* les tests unitaires faciles à écrire (par exemple, la macro [`with-redefs`](https://clojuredocs.org/clojure.core/with-redefs) peut être utilisée pour "mocker" des functions)

Ce que j'ai moins aimé :

* la découverte de certaines erreurs à l'exécution, sans comprendre directement la cause de l'erreur (du genre : stack trace obscure)
* la documentation intégrée dans le langage ne contient pas assez d'exemples à mon goût. J'ai dû souvent avoir recourt à internet et notamment à [Clojure Docs](https://clojuredocs.org/) où les exemples sont nombreux et utiles.

<br/>
## Et ensuite ?

Cet projet m'a donné envie d'explorer d'autres pistes :

* utiliser les API [GraphQL de GitHub](https://docs.github.com/en/graphql)
* transformer la ligne de commande _hubstats_ en application web (via [ClojureScript](https://clojurescript.org/) ?)
* faire un autre outil en ligne de commande
* essayer un autre langage (par exemple : [Go](https://golang.org/) ou [Rust](https://www.rust-lang.org/))
[mise à jour, 2024-12-30 : le lien GitHub GraphQL, étant cassé, a été mis à jour]

La suite au prochain épisode ! 😉
