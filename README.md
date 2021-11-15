# README

This is my blog content, in markdown format, and the configuration for static
site generation.


## Install static site generator

- Install Pelican static page generator, see http://docs.getpelican.com/en/latest/install.html.
On Mac OS, with `Homebrew`:

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
git clone --recursive https://github.com/getpelican/pelican-themes pelican-themes
```

## Generate local site

Uncomment `RELATIVE_URLS = True` in `pelicanconf.py` in order to have relative links for CSS/images/articles.

Generate content:

```sh
pelican content
```

Serve content of http://localhost:8000/:

```sh
pelican --listen
```
