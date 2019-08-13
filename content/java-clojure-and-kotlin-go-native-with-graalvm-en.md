Title: Java, Kotlin and Clojure go native with GraalVM
Date: 2019-08-13
Tags: java clojure kotlin native graalvm jvm
Slug: java-clojure-and-kotlin-go-native-with-graalvm
Author: Nicolas Kosinski
Summary: Generate native executables via GraalVM for Java, Kotlin and Clojure CLI tools
Lang: en

[Presumed audience](https://v4.chriskrycho.com/2018/assumed-audiences.html) : developers interested in the Java ecosystem and more specifically on deploying executable programs that are fast and efficient.

Plan :

1. Introduction
2. Our tools
3. An optimized executable for a "WordCount" `Java` CLI tool
4. An optimized executable for a `Kotlin` CLI tool
5. An "not-fully optimized" executable for a `Clojure` CLI tool
6. Conclusion

## Introduction

In wrote about failures in my previous blog post [Clojure goes native with GraalVM](https://nicokosi.github.io/clojure-goes-native-with-graalvm-en.html). This post is about successful attempts to generate executables from small CLI tools, implemented in [Java](https://go.java/), [Kotlin](https://kotlinlang.org/) and [Clojure](https://clojure.org/), using [GraalVM](https://www.graalvm.org/) release (see the [release notes](https://www.graalvm.org/docs/release-notes/)).

## Tools

We will use the following applications:

- [GraalVM Community Edition](https://www.graalvm.org/downloads/) ("_a High-performance polyglot VM_") and more specifically, the [Native Image](https://www.graalvm.org/docs/getting-started/#native-images) functionality (via the `native-image` command) in order to generate native executables from Java code.
- [SDKMAN!](https://sdkman.io/) ("_The Software Development Kit Manager_") in order to use several _Java Development Kits_ / _Java Runtime Environments_.
- [time](http://manpages.ubuntu.com/manpages/cosmic/en/man1/time.1.html) ("_run programs and summarize system resource usage_") in order to measure runtime durations.
- [valgrind](http://valgrind.org/) ("_tool for memory debugging, memory leak detection, and profiling_") in order to evaluate the memory footprints.

## An optimized executable for a "WordCount" `Java` application

Our "hello world" is a 10-line program that counts the number of distinct words in a text file: [wordcount-with-java-stream](https://github.com/nicokosi/wordcount-with-java-stream).

Let's generate an executable JAR file via Maven and OpenJDK. It takes 2 seconds on my machine:

```sh
$ sdk use java 8.0.222.hs-adpt
Using java version 8.0.222.hs-adpt in this shell.
$ time ./mvnw clean --quiet compile
./mvnw clean --quiet compile  6.24s user 0.31s system 323% cpu 2.022 total
```
Note that the ellapsed time is at the end of the last line, in seconds: `2.022 total` means 2.002 seconds.

Now generate an executable via GraalVM native-image. It takes 42 seconds on my machine:
```sh
$ time $HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image \
     --enable-https \
     --no-fallback \
     --no-server \
     -cp target/classes org.nicokosi.WordCount \
     wordcount-with-java-stream
$HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image --enable-https   -c  236,70s user 2,75s system 566% cpu 42,285 total
```
Let's compare the runtime durations for a small input file:
```sh
$ alias wordcount_java=" $HOME/.sdkman/candidates/java/8.0.222.hs-adpt/bin/java -cp target/classes org.nicokosi.WordCount"
$ time wordcount_java /etc/hosts
File /etc/hosts contains 26 words
/home/nkosinski/.sdkman/candidates/java/8.0.222.hs-adpt/bin/java -cp     0,16s user 0,02s system 152% cpu 0,118 total
```
```sh
$ time ./wordcount-with-java-stream /etc/hosts
File /etc/hosts contains 26 words
./wordcount-with-java-stream /etc/hosts  0,00s user 0,01s system 92% cpu 0,007 total
```
And the memory footprints:

```sh
$ JAVA_HOME=$HOME/.sdkman/candidates/java/8.0.222.hs-adpt \
  valgrind java -cp target/classes org.nicokosi.WordCount /etc/hosts

==23352== HEAP SUMMARY:
==23352==     in use at exit: 34,892,297 bytes in 6,155 blocks
==23352==   total heap usage: 14,555 allocs, 8,400 frees, 49,960,719 bytes allocated  **
```
Note that the amount of allocated memory is at the end of the last line, in bytes: `49,960,719 allocated` means that 50 megabytes have been allocated.

```sh
$ valgrind ./wordcount-with-java-stream /etc/hosts

==23753== HEAP SUMMARY:
==23753==     in use at exit: 10,468 bytes in 3 blocks
==23753==   total heap usage: 8 allocs, 5 frees, 12,436 bytes allocated**
```

To sum up, at the cost of a longer compilation (42 seconds instead of 2 seconds), GraalVM:

- speeds up our application: 7 milliseconds instead of 118 milliseconds ;
- reduces the memory footprint: 12 kilobytes instead of 50 megabytes.

## An optimized executable for a `Kotlin` CLI tool

Now let's generate an executable for a [Kotlin](https://kotlinlang.org/) CLI tool, [pullpitoK](https://github.com/nicokosi/pullpitoK/) (200 lines of code, with third-party libraries) that calls GitHub API to display information on GitHub pull requests.

The cost of compilation is similar, so let's focus on comparing the runtime behavior for a short execution (we will display the ["usage message"](https://en.wikipedia.org/wiki/Usage_message)):

```sh
$ export PATH=$HOME/.sdkman/candidates/java/8.0.222.hs-adpt/bin:$PATH
$ time (java -jar ./build/libs/pullpitoK-all.jar | head -1)
Usage: pullpitoK <repository> <token>
( java -jar ./build/libs/pullpitoK-all.jar | head -1; )  0.08s user 0.02s system 108% cpu 0.093 total
```

```sh
$ alias pullpitoK="PULLPITOK_LIBSUNEC=$HOME/.sdkman/candidates/java/19.1.1-grl/jre/lib ./pullpitoK"
$ time (pullpitoK --help | head -1)
Usage: pullpitoK <repository> <token>
( PULLPITOK_LIBSUNEC=/Users/nicolas/.sdkman/candidates/java/19.1.1-grl/jre/li)  0.00s user 0.00s system 88% cpu 0.009 total
```

So, 9 milliseconds for the native version versus 93 milliseconds for the JVM version.

Now let's compare the memory footprints:

```sh
$ valgrind java -jar ./build/libs/pullpitoK-all.jar
...
Usage: pullpitoK <repository> <token>
...
==26273== HEAP SUMMARY:
==26273==     in use at exit: 32,181,758 bytes in 2,134 blocks
==26273==   total heap usage: 5,725 allocs, 3,591 frees, 33,187,784 bytes allocated
...
```

```sh
$ valgrind pullpitoK | head -1
...
Usage: pullpitoK <repository> <token>
...
==27690== HEAP SUMMARY:
==27690==     in use at exit: 228 bytes in 1 blocks
==27690==   total heap usage: 6 allocs, 5 frees, 2,196 bytes allocated
...
```

So, 2 kilobytes for the native version versus 33 megabytes for the JVM version.

## An "not-fully optimized" executable for a `Clojure` CLI tool

When I wrote my previous article [Clojure goes native with GraalVM](https://nicokosi.github.io/clojure-goes-native-with-graalvm-en.html), GraalVM was still experimental (_release candidates_). Moreover, I was stuck with the [Native Image limitations](https://github.com/oracle/graal/blob/master/substratevm/LIMITATIONS.md) with dynamic class loading, the refection API (`java.lang.reflect`).

Let's try again with GraalVM release for a Clojure CLI tool: [hubstats](https://github.com/nicokosi/hubstats/) (200 lines of code, with third-party libraries).

```sh
$ time $HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image \
   --enable-https \
   --no-fallback \
   --no-server \
   -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar \
   hubstats
```
Native compilation fails:
```
Error: Unsupported features in 4 methods
Detailed message:
Error: Unsupported type java.lang.invoke.MemberName is reachable: All methods from java.lang.invoke should have been replaced during image building.
To diagnose the issue, you can add the option --report-unsupported-elements-at-runtime. The unsupported element is then reported at run time when it is accessed the first time.
...
```

We could probably change the source code to fix this issue. As quick fix, let's try the `fallback` mode that embeds a classic virtual machine:

```sh
$ time $HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image \
   --enable-https \
   --force-fallback \
   --no-server \
   -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar \
   hubstats
...
[hubstats:31661]      [total]:  14,663.95 ms
Warning: Image 'hubstats' is a fallback image that requires a JDK for execution (use --no-fallback to suppress fallback image generation).
$HOME/.sdkman/candidates/java/19.1.1-grl/bin/native-image --enable-https       78,73s user 1,31s system 536% cpu 14,926 total
```

With the fallback mode, duration times are similar since the startup time cannot be reduced in the native mode:

```sh
$ export PATH=$HOME/.sdkman/candidates/java/8.0.222.hs-adpt/bin:$PATH
$ time (java -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar | head -1)
Display statistics for GitHub pull requests.
( java -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar | head -1; )  3,36s user 0,10s system 262% cpu 1,318 total
```

```sh
$ time (./hubstats | head -1)

Display statistics for GitHub pull requests.
( ./hubstats | head -1; )  2,86s user 0,14s system 236% cpu 1,272 total

```

but the memory footprint of the executable is still reduced:

```sh
$ export PATH=$HOME/.sdkman/candidates/java/8.0.222.hs-adpt/bin:$PATH
$ valgrind java -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar
...
Display statistics for GitHub pull requests.
...
==2690== HEAP SUMMARY:
==2690==     in use at exit: 38,656,326 bytes in 34,800 blocks
==2690==   total heap usage: 170,569 allocs, 135,769 frees, 406,386,571 bytes allocated
...
```
```sh
$ valgrind pullpitoK
...
Usage: pullpitoK <repository> <token>
...
==5747== HEAP SUMMARY:
==5747==     in use at exit: 228 bytes in 1 blocks
==5747==   total heap usage: 6 allocs, 5 frees, 2,196 bytes allocated
...
```

## Conclusion

With these three small applications implemented with distinct JVM languages (Java, Kotlin and Clojure), we have checked some values of GraalVM native images:

- **compact executables** that can be deployed without a Java Virtual Machine
- **small memory footprints**
- **fast startup** (sometimes!).

Moreover, we can see that GraalVM will probably modernize Java for the **cloud-computing** and for **micro-services**, with the Java Runtime Environment or with frameworks like [Quarkus](https://quarkus.io/) and [Micronaut](https://micronaut.io/)).



PS: thanks to my colleagues at [Vidal](http://www.vidalfrance.com/), notably Viviane, Marc and Jean-Christophe for the discussions on GraalVM, and Stéphane for reviewing the french version of this article.