Title: Versionner sa configuration système via des "dotfiles"
Date: 2016-08-17 00:00
Tags: tools
Slug: dotfiles
Author: Nicolas Kosinski
Summary: Pourquoi et comment versioner sa configuration système (système d'exploitation, shell et applications).
Lang: fr

## Introduction : la puissance du shell, avec ou sans maîtrise ?

Cela fait environ deux ans que je développe sur un poste "\*nix" (Linux et Mac) après avoir développé de nombreuses années sur un poste Windows. La puissance du shell est indéniable : combiner des lignes de commandes simples, bénéficier de l'historique des commandes lancées, etc. Pourquoi ne pas en profiter pour maîtriser davantage son système en __versionnant sa configuration__ ?


## Présentation : Dotfiles, quezako ?

Pour un système \*nix (Linux, Mac, etc.), la configuration du shell et des applications est généralement centralisée dans les "dotfiles", des fichiers / répertoires dont le nom commence par un point ("dot" en anglais) et qui sont chargés en début de session interactive ou au lancement d'applications. En utilisant un gestionnaire de sources et des liens symboliques, on peut facilement **historiser** et **synchroniser** l'évolution de ces dotfiles afin de :

- __personnaliser le système d'exploitation__  : options d'affichage (exemple : choisir de masquer automatiquement la barre des applications), audio, etc.

- __personnaliser son shell__ :

    - positionnement de variables d'environnement (exemples : `PATH`, `JAVA_HOME`, `MVN_OPTIONS` etc.)

    - création d'alias pour les commandes fréquemment utilisées et/ou dures à mémoriser (exemple : `alias mcist="mvn clean install -DskipTests"`)

    - utilisation d'un shell "sur-vitaminé" du type [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh)

- __gérér les applications installées__, à condition d'utiliser un gestionnaire de paquets du type `homebrew` (ou `apt`, `OneGet` etc.).


## Comment ? Un exemple d'utilisation du mini-framework "holman/dotfiles"

On peut créer son propre environnement ou bien utiliser un framework "dotfiles" prêt à l'emploi car il existe de nombreux frameworks "dotfiles", en voici une liste non-exhaustive : [https://dotfiles.github.io/](https://dotfiles.github.io/).

J'ai pour ma part utilisé [https://github.com/holman/dotfiles](https://github.com/holman/dotfiles) qui permet de gérer sa configuration `ZSH` en proposant les fonctionnalités suivantes :

- chargement automatique des fichiers nommés `*.zsh`, quel que soit leur répertoire, favorisant ainsi une structure thématique. Par exemple, on peut distinguer la configuration du compilateur Java, dans le script `java/env.zsh`, de la configuration du compilateur Go, dans le script `golang/env.zsh`. Cette approche thématique remplace avantageusement l'utilisation d'un script monolithique.

- création de liens symboliques ("symlinks") pointant vers les scripts de démarrage du shell (exemple : le fichier `$HOME/.zshrc` pour le shell `ZSH`).

Après avoir "forké" [https://github.com/holman/dotfiles](https://github.com/holman/dotfile), j'ai créé deux branches :

- une pour mon ordinateur personnel sous Mac : [https://github.com/nicokosi/dotfiles](https://github.com/nicokosi/dotfiles)

- une autre pour mon ordinateur professionnel sous Linux : [https://github.com/nicokosi/dotfiles/tree/vidal](https://github.com/nicokosi/dotfiles/tree/vidal)
Ces branches me permettent d'avoir deux configurations bien distinctes même si elles partagent certaines similitudes.


## Conclusion : _Dotfiles all the things_!

Même si la mise en place et la maintenance de ses dotfiles prend du temps, l'investissement vaut le coup pour notamment :

- __la résolution de problèmes__ (exemples : identifier ce qui a été récemment modifié, revenir à une configuration précédente, etc.) ;

- __synchroniser__ des changements entre plusieurs machines (exemple : PC sous Linux au travail et Mac perso), chacune ayant  une configuration distincte ;

- __partager__ sa configuration avec d'autres développeurs ("Voici le dernier réglage que j'ai utilisé pour ...").
:

PS : merci à Jean-Christophe Gay pour l'inspiration et les "bons tuyaux". Voici son blog : [https://jeanchristophegay.com/](https://jeanchristophegay.com/).
