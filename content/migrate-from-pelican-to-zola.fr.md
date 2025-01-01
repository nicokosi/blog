+++
title = "Migration de Pelican à Zola, comme générateur de pages statiques pour mon blog"
description = "Comment j'ai mis au goût du jour le visuel de mon blog en utilisant le générateur de pages statiques Zola à la place de Pelican"
date = 2024-12-31
[taxonomies]
tags = ["blog", "static-page-generator", "migration"]
+++
# Migration de Pelican à Zola comme générateur de pages statiques

Lectorat présumé : personnes intéressées par les générateurs de pages statiques, par exemple pour écrire leur blog
personnel et le publier en ligne.

## Pourquoi migrer ?

Même si je ne publie que deux billets de blog par an, en moyenne, j'ai créé ce blog il y a 8 ans en utilisant un
générateur de pages statiques open source assez utilisé : [Pelican](https://docs.getpelican.com/).

J'avais deux "problèmes" :
1. Pelican est un outil Python et il m'est arrivé plusieurs fois qu'il ne fonctionne plus (j'avais probablement
"cassé" mon environnement de développement Python)
2. les liens vers mes profils de réseaux sociaux n'étaient pas à jour : je voulais remplacer le lien Twitter/X par des
liens vers mon profil Mastodon et Bluesky.

## Comment choisir ?

Un peu au flair, pour être honnête... 😇

Il y a quelques années (en 2021), j'avais commencé à utiliser [Hugo](https://gohugo.io/) dans [cette migration Pelican vers Hugo](https://github.com/nicokosi/blog/pull/1) que je n'ai pas terminée.

Cette année (2024), je me suis reposé la question. Au hasard de ma veille technique, j'ai entendu parler de [Zola](https://www.getzola.org/), qui
est similaire à Hugo.

Hugo comme Zola (vous voyez les références 😉) sont gratuits et "à code ouvert" (leur code est _open source_, disponible sur GitHub et ouverts aux contributions externes).

Zola étant plus récent, je me suis dit que les thèmes seront encore plus modernes et peut-être davantage maintenus... 🤷

Dans tous les cas, je pense que l'un comme l'autre peuvent faire l'affaire, comme de nombreux autres outils similaires.

Par curiosité, voici une liste de générateurs similaires, filtrable par langage d'implémentation, type de patron (_templating_), popularité GitHub (nombre d'étoiles aka _stars_) et type de licence : https://jamstack.org/generators/.

## La migration

L'interface (options de lignes de commande et méta-données) étant très proche, j'ai :

1. choisi un thème, ça peut prendre un certain temps (les goûts et les couleurs)... 😅 j'en ai essayé quelques-uns et j'ai choisi [Apollo](https://github.com/not-matthias/apollo) : je le trouve simple et joli, il semble maintenu et il gère les liens vers les réseaux sociaux Mastodon et Bluesky.
2. migré un seul article multilingue (versions française et anglaise) contenant des images ; ça m'a pris plus d'une heure, surtout pour comprendre comme gérer la version multilingue et les images.
En dehors de la configuration globale, il a fallu transformer les méta-données qui était de ce type :
```
Title: Quelques astuces shell "unix-like" que j'utilise dans mon terminal 🧙
Date: 2024-11-28 06:52
Modified: 2024-12-18 07:00
Tags: shell terminal cli tui
Slug: nix-terminal-tricks
Author: Nicolas Kosinski
Summary: astuces shell "unix-like"
Lang: fr
```
à ce format (ce qui ce fait rapidement en copiant-collant) :
```
+++
title = "Quelques astuces shell \"unix-like\" que j'utilise dans mon terminal 🧙"
description = "astuces shell \"unix-like\""
date = 2024-11-28
updated = 2024-12-18
[taxonomies]
tags = ["shell", "terminal", "cli", "tui"]
+++
```
3. migré toutes les pages (une trentaine) en modifiant "à la main" nom des fichiers et les méta-données (environ une heure)

Aperçu avant la migration (le générateur de pages statique est Pelican avec le thème) :

Aperçu après la migration :

Pour plus d'information, les détails de la migration sont dans cette _pull request GitHub_ : https://github.com/nicokosi/blog/pull/11

## Bonus

J'en ai profité pour [corriger les liens cassés](https://github.com/nicokosi/blog/pull/11/commits/5b6557350db88fcade375ed9a81905659fb57e89), détectés avec ce super outil, [Lychee](https://github.com/lycheeverse/lychee).
La règle du boy scout ("on laisse le camp plus propre en partant") appliquée au blog ! 🤓
