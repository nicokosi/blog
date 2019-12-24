Title: Rediscovering Golang with "pullpigo", a small hobby-project
Date: 2019-12-24 07:00
Tags: golang native
Slug: rediscovering-Golang-with-pullpigo
Author: Nicolas Kosinski
Summary: Learn basics of the Go programming language coding a CLI tool, "pullpigo"
Lang: en

# Rediscovering Golang with "pullpigo", a small hobby-project

I wanted to __learn [Go (the programming language)](https://golang.org/)__. My plan was to implement a __CLI tool__ for displaying information on GitHub pull requests. I thus created a small project in GitHub: [pullpigo](https://github.com/nicokosi/pullpigo), in order to display event counters about GitHub pull requests via GitHub's public API.

Note that I have already implemented this CLI tool in other programming languages that I wanted to learn: in __Clojure__ (see [hubstats](https://github.com/nicokosi/hubstats)), __Kotlin__ (see [pullpitoK](https://github.com/nicokosi/pullpitoK)) and __Rust__ (see [pullpito](https://github.com/nicokosi/pullpito)).

## Native executables are fast 🚀

Let's compile pullpigo:

```shell
$ go clean
$ time go build
go build  1.05s user 0.58s system 105% cpu 1.559 total
```
Then run it:
```shell
time ./pullpigo -repo=vidal-community/atom-jaxb
GitHub repository 'vidal-community/atom-jaxb'
  2 events created by amairi
  1 events created by fchetouani
  6 events created by AElMehdiVidal
  3 events created by jcgay
./pullpigo -repo=vidal-community/atom-jaxb  0.07s user 0.03s system 20% cpu 0.482 total
```

Now compare these build & run times with a similar Kotlin project ([pullpitoK](https://github.com/nicokosi/pullpitoK/)):
```shell
$ ./gradlew clean
$ time ./gradlew build --quiet
./gradlew build --quiet  1.37s user 0.17s system 39% cpu 3.932 total
$ time ./gradlew run --quiet --args "vidal-community/atom-jaxb"

pull requests for "vidal-community/atom-jaxb" ->
            opened per author
                amairi: 1
            commented per author
                AElMehdiVidal: 1
                jcgay: 1
            closed per author

./gradlew run --quiet --args "vidal-community/atom-jaxb"  1.37s user 0.18s system 62% cpu 2.473 total
```
Fast compilation + fast runtime = ❤️

## Golang SDK already includes many common utilities 📦

In order to call [GitHub's REST API v3 'events' API](https://developer.github.com/v3/activity/events/), all I needed was: a HTTP client, a JSON parser and a test framework. Good news, all are included in the Golang SDK: [testing](https://golang.org/pkg/testing/), [HTTP client](https://golang.org/pkg/net/http/) and [JSON parsing](https://golang.org/pkg/encoding/json/).

As a consequence, I implemented my project with zero dependencies!

Other goodies have I appreciated from by Java background:

- __code formatting__ is included! Its' simple as `go fmt`. No need to find and configure an external code formatting tools.

- __code linter__ is included! Just install [https://github.com/golang/linttype]([golang/linttype) and run the `golint` command. No need to find and configure an external code formatting tools. (to be honest, the linter did not help when coding pullpigo but it's so cool that code linter is provided).

## Other opportunities 😎

Coding this small hobby project has also been an opportunity to **try and learn other tools**. In my case, I could:

- Use [Visual Studio Code](https://code.visualstudio.com/), an Integrated Development Environment that I don't use at work.

- Use [GitHub Actions](https://github.com/features/actions) for Continuous Integration: every git commit pushed on GitHub triggers a compilation & test check. It was the first time I used GitHub Actions, it was very easy (it only took a few minutes) to use it for my needs, and it's free. 

The last positive thing about learning a programming language is that you can **discuss and learn with people** you know.

In my case, my "Golang friends" have been:

- [Jean-Christophe](https://github.com/jcgay/) who helped me to fix my JSON parsing issues. 😅

- [Florent](https://github.com/fbiville) who gave me pointers on cool libraries: [testing/quick](https://golang.org/pkg/testing/quick/) for property-based testing, [ginkgo](https://github.com/onsi/ginkgo) for BDD-style tests and [gomega](https://github.com/onsi/gomega) for test assertions. I have to try them out! 😎

### What's next? 🔮

Some ideas:

- Make pullpigo's output more useful. For example, I could make it display counters for events like "pull request created", "pull request merged" etc.

- Retrieve data from [GitHub's GraphQL API v4](https://developer.github.com/v4/) in order to by-pass the limitation of number of events (GitHub's REST API v3 'events' API only returns the last 300 events).

- Use some dependencies for testing (easier assertions, property-based-testing etc.) and take this opportunity to discover dependencies in Golang.

We'll see!