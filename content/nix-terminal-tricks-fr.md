Title: Quelques astuces shell *nix que j'utilise dans mon terminal 🧙
Date: 2024-11-28 06:52
Tags: nix shell terminal cli tui
Slug: nix-terminal-tricks
Author: Nicolas Kosinski
Summary: Quelques commandes shell "unix-like" que j'utilise souvent
Lang: fr
# Quelques astuces shell *nix que j'utilise dans mon terminal 🧙

Public présumé : dévelopeurs.ses utilisant leur terminal pour diverses tâches

Je suis un développeur qui utilise mon terminal. Voici quelques commandes / utilitaires que j'utilise régulièrement. Peut-être que ça peut vous être utile ou que vous pourrez me donner votre avis ?


## l'anti-sèche `tldr` 📝

On ne peut retenir les options de toutes les commandes. Personnellement, j'aime avoir une sorte d'anti-sèches directement dans mon terminal, sans utiliser ni mon navigateur web, ni un outil d'intelligence artificielle comme ChatGPT. 


Pour ça, j'utilise souvent [tldr](https://tldr.sh) comme une anti-sèche, c'est très pratique !

Par exemple, la commande `tldr npm` affiche :

```
  JavaScript and Node.js package manager.
  Manage Node.js projects and their module dependencies.
  More information: <https://www.npmjs.com>.

  Create a `package.json` file with default values (omit `--yes` to do it interactively):

      npm init -y|--yes

  Download all the packages listed as dependencies in `package.json`:

      npm install

  Download a specific version of a package and add it to the list of dependencies in `package.json`:

      npm install package_name@version

  Download the latest version of a package and add it to the list of dev dependencies in `package.json`:

      npm install package_name -D|--save-dev

  Download the latest version of a package and install it globally:

      npm install -g|--global package_name

  Uninstall a package and remove it from the list of dependencies in `package.json`:

      npm uninstall package_name

  List all locally installed dependencies:

      npm list

  List all top-level globally installed packages:

      npm list -g|--global --depth 0
```

### aliases 📛

### aliases à la demande

TODO

## alias permanents

Cas d'utilisation : éviter de taper de nombreuses fois la même commande que j'utilise de façon intensive pendant une période donnée.


Par exemple, je n'utilise pas souvent Docker en ligne de commandes, mais il peut m'arriver de l'utiliser plusieurs dizaines de fois pendant une heure, si j'investigue un problème ou si je définis une image via un fichier Dockerfile.
Dans ce cas, je peux être amené à créer un alias Unix qui ne dure que le temps de ma session, puis je taperai les différents commandes en utilisant cet alias :

```sh
alias d=docker
d ps
d images
# etc.
```

## filtrer la sortie 🔎

### avec `grep`

L'utilisation de _pipe_ Unix avec la commande `grep` ou ses équivalents comme [ag, "the silver searcher"](https://github.com/ggreer/the_silver_searcher) est bien utile quand je sais quoi chercher.

Par exemple, j'utilise souvent la commande `df -h | grep disk1s1` pour connaître l'espace disque restant sur mon disque dur.

### avec `fzf`, le "command-line fuzzy finder"

Quand je ne sais pas précisement quoi chercher, j'utilise souvent [fzf, the "command-line fuzzy finder"](https://junegunn.github.io/fzf/).

Par exemple, quand je veux connaître la liste des environnements Java (_Java Development Kits_) que j'ai installés, je lance peux taper la commande `sdk list java | fzf` :

![Utilisation de 'fzf' pour filtrer la commande 'sdk'](images/nix-terminal-tricks-fzf-sdk.gif")

Et pour copier plusieurs lignes, l'option `--multi` (ou sa version courte `-m`) est pratique.

Par exemple, `eza ~ | fzf -m` affiche :

![Utilisation de 'fzf' pour filtrer et selectionner plusieurs lignes de la commande 'eza'](images/nix-terminal-tricks-fzf-m-eza.gif")

## les _TUIs_, pour aller plus vite ! ⚡️

J'utilise plusieurs commandes de type [_Text-based User Interfaces_ (ou _Terminal-based_)](https://en.wikipedia.org/wiki/Text-based_user_interface), souvent désignées par le sigle _TUI_ :
- [tig](https://jonas.github.io/tig/) pour explorer rapidement les commits Git (même si j'utilise aussi la commande `git` dans mon terminal, ainsi que l'intégration Git de mon environnement de développement (_IDE_).)
- [lazydocker](https://github.com/jesseduffield/lazydocker) pour manipuler des containers Docker rapidement (même j'utilise aussi la commande `docker` directement)
- [diskonaut](https://github.com/imsnif/diskonaut) pour faire du ménage sur mon disque dur
- [l'extension GitHub CLI `user-stars`]([url](https://github.com/korosuke613/gh-user-stars?tab=readme-ov-file)) pour retrouver des dépôts GitHub auxquels j'ai mis une "étoile" (sorte de favori)
