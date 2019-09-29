+++
title = "Découvrons Rust"
date = "2018-06-10T1500"
description = "Découvrons le langage de programmation Rust en développant un petit projet personnel"
slug = "discovering-rust"
tags = [ "rust" ]
+++

_En tant que développeur.se Java, je veux découvrir Rust, de façon à bien comprendre la phrase suivante citée de [rust-lang.org](https://www.rust-lang.org)*:_
> Rust is a systems programming language that runs blazingly **fast**, **prevents segfaults**, and **guarantees thread safety**

*: avez-vous remarqué le "agile stories meme" ? 😉


## Comment j'ai commencé à apprendre Rust

[The Rust Programming Language (2nd edition)](https://doc.rust-lang.org/stable/book/second-edition/) est un chouette un livre en ligne avec des exemples concrets de petits projets implémentés pas-à-pas (un outil en ligne de commande et un serveur web).

Après avoir lu partiellement ce livre, j'ai "porté" en Rust un projet personnel nommé [hubstats](https://github.com/nicokosi/hubstats). Hubstats est un outil en ligne de commande que j'ai écrit en Clojure, qui utilise une API REST GitHub pour afficher des informations sur les pull requests GitHub dans la sortie standard. J'ai baptisé le projet Rust [pullpito](https://github.com/nicokosi/pullpito/).


Ce portage a été une façon ludique et facile d'apprendre Rust car je n'ai eu ni à réfléchir au "quoi" (afficher des informations sur le pull requests GitHub), ni au "comment" (appeler l'API GitHub que j'avais déjà utilisée dans le projet existant) : je me suis uniquement foculisé sur l'implémentation en Rust.


## Mes premières impressions

Le code Rust, ça **dépote sévère** ! Comparons par exemple l'exécution des tests unitaires `pullpito`, qui se lancent en une demi seconde :
```text
pullpito $> time (cargo test --quiet)

running 8 tests
# couic
test result: ok. 8 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

( cargo test --quiet; )  0.43s user 0.21s system 96% cpu 0.665 total
```
Alors que les tests unitaires de `hubstats` se lancent en 10 secondes :
```text
hubstats $> time (lein test)
# couic

Ran 3 tests containing 20 assertions.
0 failures, 0 errors.
( lein test; )  10.86s user 0.70s system 129% cpu 8.923 total
```

_Note: la commande `cargo` lance [Cargo](https://github.com/rust-lang/cargo/), l'outil de build de Rust ; la commande `lein` lance [Leiningen](https://leiningen.org/), un des outils de build de Clojure._

Comparons désormais les temps d'exécutions des lignes de commande. `pullpito` se lance en 20 millisecondes sur ma machine :
```text
pullpito $> time (cargo run --quiet python/peps)
pull requests for "python/peps" ->
  opened per author:
    brainwane: 1
  commented per author:
    the-knights-who-say-ni: 1
    stevendaprano: 2
    pradyunsg: 2
    gvanrossum: 1
    6502: 1
    Rosuav: 1
    brainwane: 1
  closed per author:
    markshannon: 1

( cargo run --quiet python/peps; )  0.22s user 0.09s system 20% cpu 1.524 total
```

...alors que `hubstats` prend une dizaine de secondes (oups, un peu d'optimisation serait nécessaire 😇) :
```text
hubstats $> time (lein run --organization python --repository peps)
pull requests for python/peps ->
	since 2018-05-15T05:35:57Z
		8 opened / 8 closed / 2 commented (15 comments)
 		opened per author:  {encukou 2, willingc 1, jdemeyer 1, gvanrossum 1, ethanhs 1, daxm 1, brainwane 1}
 		comments per author:  {tim-one 4, ethanhs 3, vlasovskikh 2, gvanrossum 2, JelleZijlstra 2, ilevkivskyi 1, Rosuav 1}
 		closed per author:  {brettcannon 4, markshannon 3, encukou 1}
( lein run --organization python --repository peps; )  11.30s user 0.77s system 66% cpu 18.160 total
```

Qu'en est-il de la **compilation** ? La première compilation est plus lente car toutes les dépendances doivent également être compilées. Sur ma machine, `pullpito` compile en 40 secondes :
```text
pullpito $> time (cargo clean && cargo build)
Compiling void v1.0.2
   Compiling byteorder v1.2.2
   Compiling serde v1.0.37
   Compiling scoped-tls v0.1.
# snip
    Finished dev [unoptimized + debuginfo] target(s) in 41.53 secs
( cargo clean && cargo build; )  213.99s user 16.77s system 552% cpu 41.788 total
```
Mais le compilateur Rust est incrémental, les compilations suivantes seront plus rapides voire immédiates si le code source ne change pas :
```text
pullpito $> cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
```
De son côté, `hubstats` compile en 40 secondes (ses dépendances ne sont pas compilées) :
```text
hubstats $> time (lein clean && lein uberjar)
# couic
( lein clean && lein uberjar; )  37.55s user 6.49s system 223% cpu 19.750 total
```

<br/>
## A propos de Rust, le langage

<br/>
### Ownership, gloups ! 😱

Rust gère la mémoire de façon particulière. Au lieu d'utiliser un ramasse-miettes (_garbage collector_) comme en Java ou une gestion manuelle comme en C/C++, la mémoire est automatiquement récupérée grâce aux [règles d'_ownership_](https://doc.rust-lang.org/book/second-edition/ch04-01-what-is-ownership.html) :

        Each value in Rust has a variable that’s called its owner.
        There can only be one owner at a time.
        When the owner goes out of scope, the value will be dropped.

Cela semble facile, mais ça l'est beaucoup moins en réalité.


N'ayant pas encore bien compris les implications du concept d'ownership, je n'irai pas plus loin sur ce sujet. Ma compréhension actuelle se limite à corriger toutes les erreurs de compilation liées aux violation des ces règles ! 😇

Pour plus de précisions, lire le chapitre ["Understanding Ownership"](https://doc.rust-lang.org/book/second-edition/ch04-00-understanding-ownership.html) de "The Rust Programming Language".

<br/>
### Immuable, par défaut 😎

Les variables sont immuables, par défaut. Elles ne peuvent pas être ré-assignées à moins d'être explicitement déclarées _mutables_ :
```rust
let name = "foo";
// name = "bar"; // Générerait l'erreur de compilation "error: re-assignment of immutable variable"

let mut changing_name = "bar";
changing_name = "baz";
```

Néanmoins, les variables immuables peut être surchargées (_shadowed_) :
```rust
let name = "foo";
let name = "bar"; // "shadowed variable"
```

<br/>
### Inférence de type 😎
L'inférence de type est bien sympathique et simplifie le code :
```rust
// le type peut être inféré :
let foo = "foo".to_string();
// ou bien spécifié :
let foo : String = "foo".to_string();
```

<br/>
### Filtrage par motif (_pattern matching_) 😎

On peut utiliser le pattern matching au lieu de if/else... et c'est cool !
```rust
let body = match body {
  Ok(body) => body,
  Err(_) => "default"
}
```

Par contre, le fait que les variables soient "empruntées" (_variable borrowing_) semble rendre le pattern matching plus dur à utiliser que dans d'autres langages (comme Scala). Se référer à [ce fil Stack Overflow](https://stackoverflow.com/questions/29926724/matching-string-cannot-move-out-of-borrowed-content). Note personnelle : creuser ce sujet.

<br/>
### Tuples, énumérations et structures 😎

Rust permet d'utiliser des tuples, des énumérations et des structures de données :

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Suite {
  CLUB, DIAMOND, HEART, SPADE
}

#[derive(Debug)] enum Rank {
  Ace, King, Queen, Jack
}

#[derive(Debug)] struct Card {
  suite: Suite,
  rank: Rank,
}
```
Testons cela avec le REPL `rusti` :
```rust
rusti=> Card { suite: Suite::CLUB, rank: Rank::King }
Card { suite: CLUB, rank: King }
```

<br/>
## Outillage

<br/>
### Pas de REPL (avec un support complet de Rust) 😢

Il n'y a pas de REPL (Read Eval Print Loop) officiel. C'est bien dommage !

[rusti](https://github.com/murarth/rusti) peut dépanner mais est limité et ne supporte pas toutes les évolutions récentes du langage.

Les REPL en ligne comme [repl.it](https://repl.it/site/languages/rust) peuvent se révéler utiles, même s'ils sont limités (par exemple, on ne peut pas toujours y importer des dépendances externes appelées `crates`).


### Gestion des dépendances (descripteur `Cargo.toml`) avec gestion sémantique (_semantic versioning_) 😎

Chaque dépendance binaires (appelée `crate`) :

- a un descripteur [versionné "sémantiquement"](https://semver.org/). Par exemple, la version de pullpito est 0.1.0, comme indiqué dans le descripteur `Cargo.toml` :
```text
pullpito $> grep "^version =" Cargo.toml
version = "0.1.0"
```

- déclare la version des ses dépendances :
```text
pullpito $> grep -A 10 "dependencies" Cargo.toml
[dependencies]
log = "0.4"
env_logger = "0.5"
futures = "0.1"
serde = "1.0"
serde_json = "1.0"
serde_derive = "1.0"
chrono = { version = "0.4", features = ["serde"] }
reqwest = "0.8"
```

Cool et concis, non ?

<br/>
### Formattage du code 😎

[rustfmt](https://github.com/rust-lang-nursery/rustfmt) est l'outil standard pour formater le code en utilisant un style par défaut :
```text
pullpito $> cat src/main.rs
fn main() {
  println! ("foo");
 let bar = "bar";
}

pullpito $> cargo fmt

pullpito $> cat src/main.rs
fn main() {
    println!("foo");
    let bar = "bar";
}
```
Plus de guerre du style "tabulation / espace" ! Cf. [https://xkcd.com/1285/](https://xkcd.com/1285/)!

<br/>
### Compilateur "user-friendly" (souvent) 😎

En cas d'erreur, le compilateur Rust compiler fait souvent des suggestions "amicales". Par exemple :
```rust
#[derive(Debug)] enum Suite { CLUB }
fn main() {
    println!("{:?}", Suite.CLUB);
}
```
génère l'erreur suivante :
```text
error[E0423]: expected value, found enum `Suite`
 --> src/main.rs:5:22
  |
5 |     println!("{:?}", Suite.CLUB);
  |                      ^^^^^
  |
  = note: did you mean to use one of the following variants?
          - `Suite::CLUB`
```


<br/>
### Outillage multi-version 😎

Rust a trois canaux de mise à jour (_release channels_): stable, beta, et nightly. On peut en utiliser un ou plusieurs. Par exemple, si un projet nécessite le "stable toolchain", un autre peut avoir besoin du "nightly". Dans ce cas, on utilise la commande `rustup` pour installer et utiliser ces deux versions.

Par exemple, installons le toolchain "nightly" :
```text
$> rustup install nightly
```
Il y a maintenant deux toolchains : `stable` (celui par défaut) and `nightly` :
```text
$> rustup show
Default host: x86_64-apple-darwin

installed toolchains
--------------------

stable-x86_64-apple-darwin
nightly-x86_64-apple-darwin

active toolchain
----------------

stable-x86_64-apple-darwin (default)
rustc 1.25.0 (84203cac6 2018-03-25)
```

On peut ensuite :

- changer le toolchain par défaut via `rustup default`
- activer un toolchain via `rustup set`
- utiliser un toolchain à la demande via `rustup run $toolchain $cmd` (exemple : `rustup run nightly cargo build`)

etc.
