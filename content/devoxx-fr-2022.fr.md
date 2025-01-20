+++
title = "Mon Devoxx France 2022"
description = "Mon résumé des deux jours passés à la conférence Devoxx France 2022."
date = 2022-04-23
update = 2024-12-30
[taxonomies]
tags = ["conference", "devoxx"]
+++
# Mon Devoxx France 2022

Cet article est un bilan des deux jours que j’ai eu la chance de passer à [Devoxx France 2022](https://www.youtube.com/playlist?list=PLTbQvx84FrARTeUA5pExVR5vjCOqWIplI) (j'y suis allé le mercredi et le jeudi).

Plutôt que de lister toutes les présentations auxquelles j’ai assisté (en mode “journal”), j’ai préféré me focaliser sur celles que j’ai aimées, en distinguant celles qui me seront a priori plus utiles de celles qui le seront probablement moins.

## Les présentations que j’ai aimées, “à appliquer tout de suite”

* Revoir les évolutions récentes de **Maven** (_wrapper_, _daemon_, _improved_ _reactor_, _build/producer POM_) dans la présentation [What's cooking in Maven?](https://www.youtube.com/watch?v=lT6FFbTfvXo).
* Découvrir des techniques pour écrire des tests unitaires plus expressifs avec **JUnit 5** (tests paramétrés avancés, éviter la duplication via des extensions, essayer de paralléliser progressivement via  `@Execution(CONCURRENT)`) dans la présentation [The unknowns of JUnit 5](https://www.youtube.com/watch?v=V6_rIa30YzE).
Cf. ce dépôt GitHub : [github.com/mikemybytes/the-unknowns-of-junit5](https://github.com/mikemybytes/the-unknowns-of-junit5).
* Découvrir la librairie [DOM Testing Library](https://github.com/testing-library/dom-testing-library) pour **tester** les composants web via le **DOM** en JavaScript/TypeScript dans la présentation [Le DOM Testing : Testez vos applications front plus facilement et efficacement !](https://www.youtube.com/watch?v=LAb4ChWG5Oc).

## Les présentations que j’ai aimées, à utiliser un jour, peut-être ?

* Être un peu sensibilisé à l’**éco-conception** et à la **“slow tech”** dans la keynote [Slow.tech : il est urgent de hacker le système !](https://www.youtube.com/watch?v=1uQPVOK45ow).
* Découvrir la librairie **JOOQ** permettant de requêtes aux bases de données avec un DSL très proche du SQL dans la présentation [JOOQ, joy of SQL](https://www.youtube.com/watch?v=5m_oE0iPJJE).
* Découvrir les **Fuzzing Tests** en Go dans la présentation [Fuzzing en Go](https://www.youtube.com/watch?v=Oyjo0krQz5M).
* Revoir / découvrir des techniques d’analyse / résolution de problèmes de **performance** avec des **containers** utilisant la JVM, dans la présentation [Remèdes aux oomkill, warm-ups, et lenteurs pour des conteneurs JVM](https://www.youtube.com/watch?v=Cepqgkwll_0) : analyse de la mémoire via des outils comme jcmd et JVisualVM, analyse de l’utilisation CPU via `Java Flight Recorder` et `Java Mission Control`, utilisation des quotas `Kubernetes`…
* Savoir qu’on peut faire du **Chaos Engineering** facilement dans **Kubernetes** via [LitmusChaos](https://litmuschaos.io/) dans [Du Chaos Engineering avec Litmus et Jenkins](https://www.youtube.com/watch?v=7zStrFuzLTs).
* Revoir l’intérêt du **flamegraph** pour optimiser des traitements dans la présentation [Into the flamegraph: From the primitives through advanced concepts](https://www.youtube.com/watch?v=_sYeDW06IyM).


## Et aussi…

* Le plaisir de revoir des anciens collègues et des connaissances, voire de discuter avec des inconnus. 😎
* C’est sympa de voir ses collègues dans un contexte différent. 😎
* L’apéro convivial du jeudi soir, toujours aussi sympa : bière, bretzel, fromage, petits canapés, vin blanc… 🍺
* Lors des sessions du jeudi soir (“Bird Of Feather”), c’était cool de voir les organisateurs demander l'avis des orateurs / participants et raconter des anecdotes historiques dans [10 ans déjà ! Devoxx France , l'envers du décors](https://www.youtube.com/watch?v=kOXJEzD8GKw) 😎

PS : merci à ma société, Vidal, à mon chef et à mon directeur de m’avoir payé ces deux jours de conférence ! ❤️

[mise à jour, 2024-12-30 : les liens vers les CFP, étant cassés, ont été remplacé par les liens des vidéos youtube]
