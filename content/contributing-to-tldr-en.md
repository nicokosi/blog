Title: Contributing to TLDR (collaborative cheatsheets for console commands)
Date: 2021-09-14 08:00
Tags: OSS cli
Slug: contributing-to-tldr
Author: Nicolas Kosinski
Summary: Some thoughts about my recent contributions to the open-source project 'tldr'.
Lang: en

Assumed audience: developers interested in Command-Line Interface tools and in contributing to Open Source Projects.

# My first contributions to the `tldr` open-source project

Since a few months, I occasionally contribute to [`tldr`](https://github.com/tldr-pages/tldr) (also known as `tldr-pages`) which describes as:

> Collaborative cheat-sheets for console commands

See my [contributions](https://github.com/tldr-pages/tldr/pulls?q=is%3Apr+author%3Anicokosi)).

This blog post lists the good and bad parts of these contributions.

## The good parts 👍

### Share my "local knowledge" 🎁

Many commands that were only in my Unix shell history or in my head are now shared to all `tldr` users… and to my-self!

I can now retrieve my favorite commands typing `tldr <command_name>`, i.e. `tldr espanso` since [my contribution #5662](https://github.com/tldr-pages/tldr/pull/5662) :

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

And it's easier that searching my shell history:

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

### A welcoming community 🤗

Contributors were welcoming and encouraged me without putting any pressure. My feelings are mainly related to the comments on _pull requests_ / _issues_, for example this kind [comment](https://github.com/tldr-pages/tldr/pull/5662#issuecomment-812137443):
> Welcome to tldr-pages, @nicokosi! ⚡ 🎉
 
However, I hardly used [the Gitter discussion board](https://gitter.im/tldr-pages/tldr). I think I'm not active enough (I contribute a few minutes / hours per week) to be able to keep up with the flow of trade!

### Learn new commands 👨‍🎓

While reviewing the contributions ([_pull requests_](https://github.com/tldr-pages/tldr/pulls)), I sometimes discovered new commands/discovered new options.

For example, I learned that it was possible to format the return of the GitHub CLI command `gh` as JSON via [this _pull request_` gh-formatting: add page # 6290`] (https://github.com / tldr-pages / tldr / pull / 6290 / files? short_path = 193df31 # diff-193df31fff2a4e88a95b3bd8732bead1fbbe8343eb8617ed1b727e4d1ba4d751):

> Formatting options for JSON data exported from gh GitHub CLI command. More information: https://cli.github.com/manual/gh_help_formatting.
> Display help about formatting JSON output from gh using jq:
> gh formatting

### Learn to compromise ⚖️

I have learned to accept feedback from others and sometimes to accept a majority opinion that is not mine.

Example: using the term `slug` in an authentication context for [this post](https://github.com/tldr-pages/tldr/pull/6108#discussion_r648835227).

## The bad parts 👎

### Time-consuming ⏳

Contributors on OSS project do this on their free time. Moreover, when collaborating on _pull requests_, everything is done writing in English, but we are not all bilingual. So collaboration/contribution is not always easy and can take time.

Example of misunderstanding ([link](https://github.com/tldr-pages/tldr/pull/6269#issuecomment-888351398)):
> Yes, it does seem that only common is shown, anyway that can be fixed since a user might think we have a lack of pages if we only show them.
> > Sorry, I don't understand after "anyway".

Example of slowness: it took a little less to integrate [this contribution, `Prevent search misses via input's placeholder / tooltip`](https://github.com/tldr-pages/tldr.jsx-fork/pull/3).

### No user feedback 🧑‍🦯

Only contributors give feedback via _pull requests_ or _issues_ GitHub.
There are no metrics such as "number of views", "rating" etc. therefore we do not really know the use of examples (which is a good thing for confidentiality)..

## What's next? 🔜

Contribute on code rather than documentation? 🧑‍💻

On this project or on another? To be continued! 🔮