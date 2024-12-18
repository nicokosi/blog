# nicokosi's blog ✍️

This is my [blog](https://nicokosi.github.io) content, in markdown format, and its configuration for static
site generation.

## Install

Install Zola:
```bash
brew install zola
```
or:
```bash
sudo port install zola
```

## Check the content

```bash
zola check
```

External links can be checked with [Lychee](https://github.com/lycheeverse/lychee/):

```bash
lychee --exclude-loopback --include "https://" content/*.md
```

## Serve the content locally

```bash
zola serve
```

The browse http://127.0.0.1:1111.

## Generate the pages

In order to generate the static content in the `public` directory:
```sh
zola build
```
