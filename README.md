# nicokosi's blog ✍️

This is my [blog](https://nicokosi.github.io) content, in markdown format, and its configuration for static
site generation.

## Install static site generator

- [Install Pelican](http://docs.getpelican.com/en/latest/install.html) static page generator.

On Mac OS, with [Homebrew](https://brew.sh):

```sh
brew install python
pip install pelican
pip install markdown
```

- Install Pelican theme:

```sh
git clone git@github.com:nicokosi/pelican-clean-blog.git
```

If needed, all themes can be installed this way:

```sh
git clone \
    --recursive https://github.com/getpelican/pelican-themes \
    pelican-themes
```

## Generate local site

Serve content on http://localhost:8000/:

```sh
pelican content \
    --listen \
    --extra-settings RELATIVE_URLS=false \
    --autoreload
```

## Generate content (before publishing)

```sh
pelican content
```
