+++
title = "Several ways to "
description = "A propos de la gestion sémantique de version ('semver') et autres façons de versionner nos logiciels"
date = 2025-12-17
updated = 2025-12-17
[taxonomies]
tags = ["version", "semver", "calver"]
+++

# Quelques façons de versionner le logiciel

En tant que développeur.se, on connaît plusieurs façons de versionner le logiciel. Ca fait du bien de se les remémorer, de leur donner un nom et aussi de trouver quelques exemples au travers de logiciels connus.

## version constante 🟰

Elle ne change jamais.

C'est "pratique" : on n'a pas besoin de savoir quelle version utiliser... mais c'est aussi casse-figure, YOLO!


Exemple : Docker tag `latest`.

## version incrémentale ±

Elle change régulièrement, par exemple en s'incrémentant de 1 à chaque nouvelle version.

Sûre, mais ne reflète pas l'impact des changements.

Exemples : Java `25`, `26` etc.

## version par identifiant #️⃣

Elle consiste en un identifiant de commit Git (empreinte SHA-1), un identifiant de type UUID, etc.

Sûre, elle permet une "infinité" de versions, mais ne reflète pas l'impact des changements.

Exemple : commit Git `a3f9c2e`.

## version sémantique 🤓

AKA _semantic versioning_ ou [_semver_](https://semver.org).

Elle introduit les concepts de :
 - version majeure : changement non rétro-compatible
 - version mineure : évolution rétro-compatible
 - version de correctif (_patch_)
 - phase de développement : alpha, beta, release candidate, release etc.

Incontournable pour une librairie, moins évidente pour une application.
Elle est précise, mais demande donc de la rigueur et est plus fragile.

Exemples : 
- Jackson `2.20.1` : le premier patch de la version mineure 20 de la version majeur 2
- Jackson `3.0.1` : le premier patch de la version mineure 0 de la version majeur 3 (qui n'est pas rétro-compatible avec la version majeur 2)

Anectode : "les joies" de _npm version range_ : [semver.npmjs.com](https://semver.npmjs.com) 😅

## version temporelle 🗓️

AKA _calendar versioning_ ou [_calver_](https://calver.org).

Correspond à une année, une version dans l'année, un mois dans l'année etc.

Facile, mais opaque.

Exemples :
- IntelliJ IDEE `2025.1` : première version de l'année 2025)
- Ubuntu `24.04` : version sortie en avril 2024

## noms semi-aléatoires 🎲

Correspond à un nom aléatoire généré à partir d'un dictionnaire.

Pratique pour nous, les humains (😊), mais opaque.

Exemple : container Docker nommé `sad_tesla`.

Cf. [documentation Docker](https://pkg.go.dev/github.com/docker/docker/pkg/namesgenerator) ([code source](https://github.com/moby/moby/blob/master/internal/namesgenerator/names-generator.go)).

## "récapitulatif" 💡

Revoyons une partie de ces types de version au moyen d'une seule commande \*nix :

```sh
# Lister toutes les applications installées sur mon Mac via Homebrew 🍺
brew list --versions

ca-certificates 2025-12-02
cargo-audit 0.22.0
clj-kondo 2025.10.23
cowsay 3.8.4
gist 6.0.0
gitlogue 0.6.0
mas 4.1.0
openssl@3 3.6.0
trash 0.9.2
calibre 8.16.2
firefox 82.0.3
firefox@nightly latest
ghostty 1.0.1
gimp 3.0.6
google-chrome 137.0.7151.56
grandperspective 3.6
handy 0.6.8
iterm2 3.4.8
jetbrains-toolbox 1.24,1.24.12080
keepingyouawake 1.6.8
kobo latest
libreoffice 25.8.3
molotov 7.0.0
openemu 2.3.3
podman-desktop 1.15.0
postman 9.5.0
rectangle 0.41,46
slack 4.11.3
sublime-text 4169
textmate 2.0.23
visual-studio-code 1.27.2,f46c4c469d6e6d8c46f268d1553c5dc4b475840f
vlc 3.0.0
warp 0.2025.07.09.08.11.stable_01
xmind 26.01.07153-202512110349
zed 0.119.18
```

Noter que certaines sont combinées / multiples.
