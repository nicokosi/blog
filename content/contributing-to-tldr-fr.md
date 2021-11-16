Title: Mes contributions à TLDR (anti-sèche collaborative pour les outils en ligne de commande)
Date: 2021-09-14 08:00
Tags: OSS cli
Slug: contributing-to-tldr
Author: Nicolas Kosinski
Summary: Quelques réflexions au sujet de mes contributions récentes au projet open-source 'tldr'.
Lang: fr

Public présumé : développeurs.euses intéressé.es par les outils en ligne de commande et à la collaboration open-source.

# Mes débuts de contribution au projet open-source `tldr`

Cela fait quelques mois que je contribue épisodiquement au projet [`tldr`](https://github.com/tldr-pages/tldr) (ou `tldr-pages`), une sorte d'anti-sèche collaborative pour commandes shell (cf. mes [contributions récentes](https://github.com/tldr-pages/tldr/pulls?q=is%3Apr+author%3Anicokosi)).
Cet article est un bilan des points positifs et négatifs de ces contributions.

## Les bons côtés 👍

### Partager ma "connaissance locale" 🎁

Certaines commandes qui faisaient partie de mon historique shell ou qui étaient dans ma tête sont maintenant partagées à tous les utilisateurs de `tldr`... et aussi à moi même !

Je peux désormais les retrouver plus facilement en tapant `tldr <nom_de_la_commande>`, par exemple `tldr espanso` depuis [ma contribution #5662](https://github.com/tldr-pages/tldr/pull/5662) :

```sh
$ tldr espanso

espanso

Cross-platform Text Expander written in Rust.
More information: <https://espanso.org>.

- Check status:
    espanso status

- Edit the configuration:
    espanso edit config

- Install a package from the hub store (<https://hub.espanso.org/>):
    espanso install package_name

- Restart (required after installing a package, useful in case of failure):
    espanso restart
```

C'est plus rapide que de chercher dans mon historique shell :

```sh
$ history | grep espanso
 4998  brew tap federico-terzi/espanso
 4999  brew install espanso
 5000  espanso register
 5001  mkdir espanso
 5002  cd espanso
 5013  espanso stop
 5014  espanso start
 5015  espanso path
```

### Une communauté accueillante 🤗

J'ai été très bien accueilli par les contributeurs qui encouragent sans mettre de pression. Mon ressenti est surtout lié aux commentaires sur les _pull requests_ / _issues_, par exemple ce genre de [commentaire](https://github.com/tldr-pages/tldr/pull/5662#issuecomment-812137443) est toujours agréable : 
> Welcome to tldr-pages, @nicokosi! ⚡ 🎉
 
Par contre, je n'ai quasimment pas utilisé [le forum de discussions Gitter](https://gitter.im/tldr-pages/tldr). Je pense que je ne suis pas assez actif (je contribue quelques minutes / heures par semaine) pour pouvoir suivre le flux des échanges !

### Apprendre de nouvelles commandes 👨‍🎓

En faisant la revue des contributions ([_pull requests_](https://github.com/tldr-pages/tldr/pulls)), j'ai parfois découvert des nouvelles commandes ou découvert de nouvelles options.

Par exemple, j'ai découvert qu'il était possible de formater en JSON le retour de la commande GitHub CLI `gh` via [cette _pull request_ `gh-formatting: add page #6290`](https://github.com/tldr-pages/tldr/pull/6290/files?short_path=193df31#diff-193df31fff2a4e88a95b3bd8732bead1fbbe8343eb8617ed1b727e4d1ba4d751) :

> Formatting options for JSON data exported from gh GitHub CLI command. More information: https://cli.github.com/manual/gh_help_formatting.
> Display help about formatting JSON output from gh using jq:
> gh formatting

### Apprendre le compromis ⚖️

J'ai appris à accepter les retours des autres et à parfois accepter un avis majoritaire qui n'est pas le mien.

Exemple : utiliser le terme `slug`dans un contexte d'authentification pour [cette contribution](https://github.com/tldr-pages/tldr/pull/6108#discussion_r648835227).

## Les "mauvais" côtés 👎

### Ca prend du temps ! ⏳

Quand on fait des suggestions aux autres sur une _pull request_ ou qu'on répond à celles des autres, tout se fait par écrit, en anglais, or je ne suis pas bilingue et les autres personnes ne le se sont pas forcement non plus... et si on ajoute le fait que les contributeurs font ça sur leur temps libre... tout prend du temps.

Exemple d'incompréhension ([lien](https://github.com/tldr-pages/tldr/pull/6269#issuecomment-888351398)) :
> Yes, it does seem that only common is shown, anyway that can be fixed since a user might think we have a lack of pages if we only show them.
> > Sorry, I don't understand after "anyway".

Exemple de lenteur : il a fallu un moins pour intégrer [cette contribution, `Prevent search misses via input's placeholder/tooltip`](https://github.com/tldr-pages/tldr.jsx-fork/pull/3).

### Pas de retours des utilisateurs 🧑‍🦯

Seules les personnes qui contribuent font des retours via les _pull requests_ ou les _issues_ GitHub.
Il n'y a pas de métriques du type "nombre de vues", "note" etc. donc on ne connaît donc pas vraiment l'usage des exemples (ce qui est une bonne chose pour la confidentialité).

## La suite ? 🔜

Contribuer sur du code plutôt que de la documentation ? 🧑‍💻
Sur ce projet ou sur un autre ? A suivre ! 🔮
