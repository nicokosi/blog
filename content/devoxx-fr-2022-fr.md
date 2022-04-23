Title: Mon Devoxx France 2022
Date: 2022-04-23 17:00
Tags: conference devoxx
Slug: devoxx-fr-2022
Author: Nicolas Kosinski
Summary: Mon résumé des deux jours passés à la conférence Devoxx France 2022.
Lang: fr

# Mon Devoxx France 2022

Cet article est un bilan des deux jours que j’ai eu la chance de passer à [Devoxx France 2022](https://cfp.devoxx.fr/2022/index.html) (cf. programmes du [mercredi](https://cfp.devoxx.fr/2022/byday/wed) et du [jeudi](https://cfp.devoxx.fr/2022/byday/thu)).

Plutôt que de lister toutes les présentations auxquelles j’ai assisté (en mode “journal”), j’ai préféré me focaliser sur celles que j’ai aimées, en distinguant celles qui me seront a priori plus utiles de celles qui le seront probablement moins.

## Les présentations que j’ai aimées, “à appliquer tout de suite”

* Revoir les évolutions récentes de **Maven** (_wrapper_, _daemon_, _improved_ _reactor_, _build/producer POM_) dans la présentation [What's cooking in Maven?](https://cfp.devoxx.fr/2022/talk/MPH-2660/What's_cooking_in_Maven%3F).
* Découvrir des techniques pour écrire des tests unitaires plus expressifs avec **JUnit 5** (tests paramétrés avancés, éviter la duplication via des extensions, essayer de paralléliser progressivement via  `@Execution(CONCURRENT)`) dans la présentation [The unknowns of JUnit 5](https://cfp.devoxx.fr/2022/talk/LKZ-8754/The_unknowns_of_JUnit_5).
Cf. ce dépôt GitHub : [github.com/mikemybytes/the-unknowns-of-junit5](https://github.com/mikemybytes/the-unknowns-of-junit5).
* Découvrir la librairie [DOM Testing Library](https://github.com/testing-library/dom-testing-library) pour **tester** les composants web via le **DOM** en JavaScript/TypeScript dans la présentation [Le DOM Testing : Testez vos applications front plus facilement et efficacement !](https://cfp.devoxx.fr/2022/talk/UHY-1828/Le_DOM_Testing_:_Testez_vos_applications_front_plus_facilement_et_efficacement_!).

## Les présentations que j’ai aimées, à utiliser un jour, peut-être ?

* Être un peu sensibilisé à l’**éco-conception** et à la **“slow tech”** dans la keynote [Slow.tech : il est urgent de hacker le système !](https://cfp.devoxx.fr/2022/talk/WEW-0145/Slow.tech_:_il_est_urgent_de_hacker_le_systeme_!_).
* Découvrir la librairie **JOOQ** permettant de requêtes aux bases de données avec un DSL très proche du SQL dans le présentation [JOOQ, joy of SQL](https://cfp.devoxx.fr/2022/talk/IQC-0059/JOOQ,_joy_of_SQL).
* Découvrir les **Fuzzing Tests** en Go dans la présentation [Fuzzing en Go](https://cfp.devoxx.fr/2022/talk/VHP-9005/Fuzzing_en_Go).
* Revoir / découvrir des techniques d’analyse / résolution de problèmes de **performance** avec des **containers** utilisant la JVM, dans la présentation [Remèdes aux oomkill, warm-ups, et lenteurs pour des conteneurs JVM](https://cfp.devoxx.fr/2022/talk/DVW-6325/Remedes_aux_oomkill,_warm-ups,_et_lenteurs_pour_des_conteneurs_JVM) : analyse de la mémoire via des outils comme jcmd et JVisualVM, analyse de l’utilisation CPU via FlightRecorder et Java Mission Control, utilisation des quotas Kubernetes…
* Savoir qu’on peut faire du **Chaos Engineering** facilement dans **Kubernetes** via [LitmusChaos](https://litmuschaos.io/) dans [Du Chaos Engineering avec Litmus et Jenkins](https://cfp.devoxx.fr/2022/talk/KLY-7038/Du_Chaos_Engineering_avec_Litmus_et_Jenkins).
* Revoir l’intérêt du **flamegraph** pour optimiser des traitements dans la présentation [Into the flamegraph: From the primitives through advanced concepts](https://cfp.devoxx.fr/2022/talk/NAN-7766/Into_the_flamegraph:_From_the_primitives_through_advanced_concepts).


## Et aussi…

* Le plaisir de revoir des anciens collègues et des connaissances, voire de discuter avec des inconnus. 😎
* C’est sympa de voir ses collègues dans un contexte différent. 😎
* L’apéro convivial du jeudi soir, toujours aussi sympa : bière, bretzel, canapé, vin blanc… 🍺
* Lors des sessions du jeudi soir, “Bird Of Feather”, c’était cool de voir les organisateurs donner retour / raconter des anecdotes historiques dans [10 ans déjà ! Devoxx France , l'envers du décors](https://cfp.devoxx.fr/2022/talk/BIT-5819/10_ans_deja_!_Devoxx_France_,_l'envers_du_decors) 😎

PS : merci à ma société, Vidal, à mon chef et à mon directeur de m’avoir payé ces deux jours de conférence ! ❤️
