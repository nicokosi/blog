+++
title = "Découvrons Rust"
date = "2018-06-10T1500"
description = "Découvrons le langage de programmation Rust en développant un petit projet personnel"
slug = "discovering-rust"
tags = [ "rust" ]
+++

_As a Java developer, I want to learn bits of Rust, so that I can deeply understand this sentence quoted from [rust-lang.org](https://www.rust-lang.org)*:_
> Rust is a systems programming language that runs blazingly **fast**, **prevents segfaults**, and **guarantees thread safety**

*: did you notice the "agile stories meme"? 😉


## How I started learning Rust

[The Rust Programming Language (2nd edition)](https://doc.rust-lang.org/stable/book/second-edition/) is a great free on-line book with pragmatic examples and small projects that are progressively implemented (a CLI tool and a web server).

After reading parts of this book, I ported a personal project named [hubstats](https://github.com/nicokosi/hubstats) from Clojure to Rust. Hubstats is a command line tool I wrote in Clojure that calls GitHub API and displays pull requests summaries in the standard output. I just converted this project in Rust: [pullpito](https://github.com/nicokosi/pullpito/).

Porting existing code was an enjoyable way to learn Rust since I did not had to think about the "what" (display pull requests information) and the "how" (call the GitHub API): I just had to focus on Rust coding!


## My first impressions

Rust code runs **fast**! For instance, let's compare running a few `pullpito`'s unit tests that run in half a second:
```text
pullpito $> time (cargo test --quiet)

running 8 tests
# snip
test result: ok. 8 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

( cargo test --quiet; )  0.43s user 0.21s system 96% cpu 0.665 total
```
On the other hand, `hubstats`' tests run in 10 seconds:
```text
hubstats $> time (lein test)
# snip

Ran 3 tests containing 20 assertions.
0 failures, 0 errors.
( lein test; )  10.86s user 0.70s system 129% cpu 8.923 total
```

_Note: the `cargo` command launches [Cargo](https://github.com/rust-lang/cargo/) which is Rust's build tool ; the `lein` command launches [Leiningen](https://leiningen.org/) which is Clojure's build tool_.

Now let's compare the CLI tool executions. `pullpito` runs in 20 milliseconds:
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

...whereas `hubstats` runs in 11 seconds (it should probably be optimized 😇):
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

What about **compilation**? The first compilation is slow because all dependencies have to be compiled. For instance, `pullpito` initially compiles in 40 seconds, on my machine:
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
But Rust has an incremental compiler, so subsequent compilations will be immediate if code does not change:
```text
pullpito $> cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
```
On the other hand, `hubstats` compiles in 40 seconds (dependencies are not compiled):
```text
hubstats $> time (lein clean && lein uberjar)
# snip
( lein clean && lein uberjar; )  37.55s user 6.49s system 223% cpu 19.750 total
```

<br/>
## About Rust, the language

<br/>
### Ownership, OMG! 😱

Rust has a particular way to manage memory. Instead of using a garbage collector like Java or manual management like C/C++, allocated memory is automatically cleaned using the ["ownership" rules](https://doc.rust-lang.org/book/second-edition/ch04-01-what-is-ownership.html):

        Each value in Rust has a variable that’s called its owner.
        There can only be one owner at a time.
        When the owner goes out of scope, the value will be dropped.

It seems easy, but in reality, all the implications are hard to understand!


Since I have not fully understood the ownership implications, I will not go any further on this topic. My current status is: fix all the compilation errors! 😇

Feel free to read more about it in the chapter ["Understanding Ownership"](https://doc.rust-lang.org/book/second-edition/ch04-00-understanding-ownership.html) of "The Rust Programming Language".

<br/>
### Immutability by default 😎

A variable is immutable, by default. It cannot be re-assigned unless explicitly declared mutable:
```rust
let name = "foo";
// name = "bar"; // Would trigger this compilation error: "error: re-assignment of immutable variable"

let mut changing_name = "bar";
changing_name = "baz";
```

However, immutable variables can be shadowed:
```rust
let name = "foo";
let name = "bar"; // shadowed variable
```

<br/>
### Type inference 😎
Type inference is great for conciseness:
```rust
// Type can be inferred:
let foo = "foo".to_string();
// or set explicitly:
let foo : String = "foo".to_string();
```

<br/>
### Pattern matching 😎

Rust has pattern matching... and it's cool!
```rust
let body = match body {
  Ok(body) => body,
  Err(_) => "default"
}
```

As far as I understand, variable borrowing makes pattern matching harder to use, as seen in the [Stack Overflow](https://stackoverflow.com/questions/29926724/matching-string-cannot-move-out-of-borrowed-content). Note to self: try this out.

<br/>
### Tuples, enums and structures 😎

Rust has enums, tuples, and structures:

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
Let's test it via the `rusti` REPL:
```rust
rusti=> Card { suite: Suite::CLUB, rank: Rank::King }
Card { suite: CLUB, rank: King }
```

<br/>
## Rust tooling

<br/>
### No REPL (with full Rust support) 😢

There is no official REPL (Read Eval Print Loop), and that's a pity for beginners like me!

[rusti](https://github.com/murarth/rusti) can help but does not support all recent language changes.

On-line REPLs such as [repl.it](https://repl.it/site/languages/rust) can also be handy, even if limited (e.g. cannot import external dependencies aka `crates`).


### Concise dependency descriptors (`Cargo.toml`) with semantic versioning 😎

Every cargo binary (aka `crate`):

- has a descriptor with a [semantic version](https://semver.org/). For instance, pullpito's version is 0.1.0, as declared in its `Cargo.toml` descriptor:
```text
pullpito $> grep "^version =" Cargo.toml
version = "0.1.0"
```

- declares the versions of its own dependencies:
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

Cool and concise, isn't it?

<br/>
### Standard code format 😎

[rustfmt](https://github.com/rust-lang-nursery/rustfmt) can be used as a command-line tool to format code using a default style:
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
No more "tabs vs space vs ..." flame war! Cf. [https://xkcd.com/1285/](https://xkcd.com/1285/)!

<br/>
### User-friendly compiler (mostly) 😎

The Rust compiler often makes useful suggestions in case of compilation error. Example:
```rust
#[derive(Debug)] enum Suite { CLUB }
fn main() {
    println!("{:?}", Suite.CLUB);
}
```
will fail compiling:
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
### A multi-version toolchain: `rustup` 😎

Rust has three release channels: stable, beta, and nightly. You can natively install and use one, some or all of them. Indeed, some libraries or tools may only work on the "stable" toolchain, and others may require the "nightly" one. In that case, use the `rustup` command to install and use both toolchains.

For instance, I can install the `nightly` toolchain:
```text
$> rustup install nightly
```
There are now two toolchains: `stable` and `nightly`:
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

I can then:

- change the default toolchain via `rustup default`
- set the active toolchain via `rustup set`
- use it on demand via `rustup run $toolchain $cmd` (example: `rustup run nightly cargo build`)

etc.
