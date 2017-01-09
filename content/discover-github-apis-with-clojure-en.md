Title: Discovering GitHub APIs while learning Clojure
Date: 2017-01-11 08:56
Tags: clojure github
Slug: discover-github-apis-with-clojure
Author: Nicolas Kosinski
Summary: Discovering GitHub APIs while learning Clojure
Lang: en

As a developer, it's important to keep on learning/discovering stuff. Quoting [The Pragmatic Programmer](https://pragprog.com/book/tpp/the-pragmatic-programmer) :
> Invest Regularly in Your Knowledge Portfolio


My last project "for learning" was to create a command-line tool, named [hubstats](https://github.com/nicokosi/hubstats), that outputs a summary for [pull requests GitHub](https://help.github.com/articles/github-glossary/#pull-request). This tool aims at giving some metrics for me and my team.

The real purposes were to practice [Clojure](https://clojure.org/) (which I knew little) but also to discover [REST](https://developer.github.com/v3/) and [GraphQL](https://developer.github.com/early-access/graphql/) GitHub APIs.

Moreover, I was lucky to interact with a colleague of mine who is an advanced Clojure developer. That was really cool, thanks Jérôme aka [@jprudent](https://github.com/jprudent)!

<br/>
## What is _hubstats_?

_hubstats_ is a simple command line tool that outputs, for a given [GitHub repository](https://help.github.com/articles/github-glossary/#repository), the number of opened/commented/merged pull requests by author for a given period (last week, since a given date, etc.).

Here is an output example:
```shell
lein run --organization softwarevidal --repository arthur --token $token
pull requests for softwarevidal/arthur ->
    since 1 week(s):
        9 opened / 56 commented / 5 closed
        opened per author: {"cmahalin" 5, "jcgay" 2, "AElMehdiVidal" 2}
        commented per author: {"vidal-rm" 30, "jcgay" 17, "cmahalin" 9}
        closed per author: {"cmahalin" 2, "AElMehdiVidal" 2, "jprudent" 1}
```

<br/>
## How does it work?

I have chosen Clojure, a language that is different from the language that I use every day (Java).

The following characteristics appealed to me:

* dynamic and interactive development: code is short and simple, which seems cool for an internal tool; what's more, the [REPL](https://clojure.org/about/dynamic#_the_repl) is a base tool that greatly fit to a discovery mindset.
* functional programming: functions are _first-class citizen_, immutability and function recursion are basics
* Lisp: Clojure is a Lisp, so writing code is a bit different from C-like languages ; Code is data and can be edited via [paredit](https://www.emacswiki.org/emacs/ParEdit) (emacs-like mode for editing code while keeping parentheses balanced).
* simplicity: Clojure encourages too use small libraries instead of huge frameworks.

See [Clojure Rationale](https://clojure.org/about/rationale).


My dev setup:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/) with [Cursive plugin](https://cursive-ide.com/)
- [Cursive _paredit_ mode](https://cursive-ide.com/userguide/paredit.html)
- [Leiningen](https://leiningen.org/) as build tool
- [Travis CI](https://travis-ci.org/) for continuous integration

<br/>
## So what?

What I liked:

* a "parenthesis" (haha!) with my daily Java routines/habits
* _paredit_ is confusing at first, then pleasant to use
* REPL rocks for
    * shaping code (acts as a draft for new code)
    * troubleshooting bugs (example: incorrect GitHub pagination traversing that led to out-of-memory crash)
* unit tests are easy to write (example: [`with-redefs`](https://clojuredocs.org/clojure.core/with-redefs) macro can be used to mock functions: https://clojuredocs.org/clojure.core/with-redefs)

What I did not like:

* WTFs when runtime bugs occurred (obscure stack traces)
* integrated documentation lacks examples. I often had to browse [Clojure Docs](https://clojuredocs.org/) to understand Clojure base functions via useful examples.

<br/>
## What's next?

Some ideas for some evolutions (or an other project, maybe?):

* use [GitHub GraphQL](https://developer.github.com/early-access/graphql/)
* make a web app for _hubstats_ (via [ClojureScript](https://clojurescript.org/)?)
* build another CLI tool
* learn another language (for example: [Go](https://golang.org/) or [Rust](https://www.rust-lang.org/))

That's all folk! 😉
