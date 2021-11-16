Title: Clojure goes native with GraalVM
Date: 2018-05-12 13:00
Tags: clojure native graalvm
Slug: clojure-goes-native-with-graalvm
Author: Nicolas Kosinski
Summary: Use GraalVM to generate native executable for 'hubstats', a Clojure project.
Lang: en


## What is GraalVM?

[GraalVM](http://www.graalvm.org/) is a virtual machine that supports several programming languages: Java, JVM-based languages (Scala, Groovy, Kotlin etc.), JavaScript, LLVM, Ruby and R. It also allows to generate native executables from Java bytecode:
```
For JVM-based languages, GraalVM offers a mechanism to create precompiled native images with instant start up and low memory footprint.
```

[Oracle labs announced in April 2018](https://blogs.oracle.com/developers/announcing-graalvm) GraalVM 1.0 release candidate, so let's have a try!


## Build a native executable for a Clojure project

[hubstats](https://github.com/nicokosi/hubstats) is my Clojure toy project for displaying statistics about GitHub pull requests. It is a command line tool that runs with a Java virtual machine, so GraalVM could bring instant startup via a native executable.

Notes:

- I have used some tips from this [interesting blog post](https://www.innoq.com/en/blog/native-clojure-and-graalvm/
).

- I have used GraalVM Community Edition, which is free and open source (Enterprise Edition also exists).

### Attempt #1

From a "fat" JAR (an archive with Java bytecode that includes all its dependencies), I ran the command `native-image` from [GraalVM 1.0.0-rc1 inside a Docker container](https://github.com/Danny02/graalvm-docker):

```sh
native-image \
  -jar hubstats-0.1.0-SNAPSHOT-standalone.jar \
  -H:+ReportUnsupportedElementsAtRuntime \
  hubstats.core
```
(see the [full details here](https://github.com/nicokosi/hubstats/pull/12/files))

Bad luck, the native image generation failed:
```
Step 4/15 : RUN native-image   -jar hubstats-0.1.0-SNAPSHOT-standalone.jar   -H:+ReportUnsupportedElementsAtRuntime   hubstats.core
 ---> Running in e7f911774bd4
Build on Server(pid: 11, port: 26681)*
   classlist:   3,159.26 ms
       (cap):   1,485.02 ms
       setup:   2,563.80 ms
    analysis:  10,109.06 ms
fatal error: java.lang.NullPointerException
	at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
	at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
	at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
	at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
	at java.util.concurrent.ForkJoinTask.getThrowableException(ForkJoinTask.java:598)
	at java.util.concurrent.ForkJoinTask.get(ForkJoinTask.java:1005)
	at com.oracle.svm.hosted.NativeImageGenerator.run(NativeImageGenerator.java:398)
	at com.oracle.svm.hosted.NativeImageGeneratorRunner.buildImage(NativeImageGeneratorRunner.java:240)
	at com.oracle.svm.hosted.NativeImageGeneratorRunner.build(NativeImageGeneratorRunner.java:337)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.executeCompilation(NativeImageBuildServer.java:378)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.lambda$processCommand$8(NativeImageBuildServer.java:315)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.withJVMContext(NativeImageBuildServer.java:396)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.processCommand(NativeImageBuildServer.java:312)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.processRequest(NativeImageBuildServer.java:256)
	at com.oracle.svm.hosted.server.NativeImageBuildServer.lambda$serve$7(NativeImageBuildServer.java:216)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	at java.lang.Thread.run(Thread.java:748)
Caused by: java.lang.NullPointerException
	at com.oracle.graal.pointsto.ObjectScanner.scanField(ObjectScanner.java:113)
	at com.oracle.graal.pointsto.ObjectScanner.doScan(ObjectScanner.java:263)
	at com.oracle.graal.pointsto.ObjectScanner.finish(ObjectScanner.java:307)
	at com.oracle.graal.pointsto.ObjectScanner.scanBootImageHeapRoots(ObjectScanner.java:78)
	at com.oracle.graal.pointsto.ObjectScanner.scanBootImageHeapRoots(ObjectScanner.java:60)
	at com.oracle.graal.pointsto.BigBang.checkObjectGraph(BigBang.java:581)
	at com.oracle.graal.pointsto.BigBang.finish(BigBang.java:552)
	at com.oracle.svm.hosted.NativeImageGenerator.doRun(NativeImageGenerator.java:653)
	at com.oracle.svm.hosted.NativeImageGenerator.lambda$run$0(NativeImageGenerator.java:381)
	at java.util.concurrent.ForkJoinTask$AdaptedRunnableAction.exec(ForkJoinTask.java:1386)
	at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:289)
	at java.util.concurrent.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1056)
	at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1692)
	at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:157)
Error: Processing image build request failed
```

I visibly hit a similar issue than [issue#385](https://github.com/oracle/graal/issues/385) and [issue#375](https://github.com/oracle/graal/issues/375). It seems to be related to the ["static initializers" limitation](https://github.com/oracle/graal/blob/master/substratevm/LIMITATIONS.md#static-initializers). 😢


### Attempt #2

Since some fixes were available in [GraalVM's GitHub repository](https://github.com/graalvm/), I tried to build `substratevm` sub-module from source.

- I grabbed GraalVM's code:
```sh
git clone git@github.com:oracle/graal.git
```
As stated in [substratevm's README file](https://github.com/oracle/graal/tree/master/substratevm), I downloaded the [GraalVM "labs" JDK](http://www.oracle.com/technetwork/oracle-labs/program-languages/downloads/index.html) then I built the 'substratevm' module that includes the 'native-image' command:
```sh
cd substratevm
JAVA_HOME=~/Downloads/labsjdk1.8.0_161-jvmci-0.42/Contents/Home ../../mx/mx build
```

I then launched the 'native-image' command but it "hanged" forever:
```
$> JAVA_HOME=~/Downloads/labsjdk1.8.0_161-jvmci-0.42/Contents/Home ../graal/substratevm/native-image -jar target/hubstats-0.1.0-SNAPSHOT-standalone.jar hubstats.core
Build on Server(pid: 18933, port: 55103)*
   classlist:   2,744.32 ms
       (cap):   1,531.16 ms
       setup:   2,401.40 ms
```
A similar issue has already been reported in GraalVM issues: ["native image failed to build jar](https://github.com/oracle/graal/issues/411). 😭


### Conclusion

Obviously, these first attempts were not successful, but GraalVM is a young project and I do not know much about it. Nevertheless, it was fun to discover GraalVM which looks promising! 😍

I will try again, stay tuned!
