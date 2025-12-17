+++
title = "Several ways to version software"
description = "About sofware versioning practises like 'semver', 'calver' etc."
date = 2025-12-17
updated = 2025-12-17
[taxonomies]
tags = ["version", "semver", "calver"]
+++
# Several ways to version software

As developers, we know several ways to version software. Let's review them and also find some examples through well-known software.

## Constant version 🟰

It never changes.

It's "practical": we don't need to know which version to use... but it's also risky, YOLO!

Example: Docker tag `latest`.

## Incremental version ±

It changes regularly, for example by incrementing by 1 for each new version.

Safe and easy.

Examples: Java `25`, `26` etc.

## Version by identifier #️⃣

It can consist of a Git commit identifier (SHA-1 hash), a UUID type identifier, etc.

Safe, it allows for an "infinity" of versions.

Example: Git commit `a3f9c2e`.

## Semantic versioning 🤓

AKA _semantic versioning_ or [_semver_](https://semver.org).

It introduces the concepts of:
 - major version: non-backward compatible change
 - minor version: backward compatible evolution
 - patch version: bug fixes
 - development phase: alpha, beta, release candidate, release etc.

Essential for a library, less obvious for an application.
It is precise, but therefore requires rigor and is more fragile.

Examples: 
- Jackson `2.20.1`: the first patch of minor version 20 of major version 2
- Jackson `3.0.1`: the first patch of minor version 0 of major version 3 (which is not backward compatible with major version 2)

Anecdote: "the joys" of _npm version range_: [semver.npmjs.com](https://semver.npmjs.com) 😅

## Calendar versioning 🗓️

AKA [_calver_](https://calver.org).

Corresponds to a year, a version within the year, a month in the year etc.

Examples:
- IntelliJ IDEA `2025.1`: first version of the year 2025
- Ubuntu `24.04`: version released in April 2024

## Semi-random names 🎲

Corresponds to a random name generated from a dictionary.

Practical for us humans (😊).

Example: Docker container named `sad_tesla`.

See [Docker documentation](https://pkg.go.dev/github.com/docker/docker/pkg/namesgenerator) ([source code](https://github.com/moby/moby/blob/master/internal/namesgenerator/names-generator.go)).

## "Summary" 💡

Let's review some of these version types using a single \*nix command:

```sh
# List all applications installed on my Mac via Homebrew 🍺
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
warp
```
