# README

This is my blog content, in markdown format, and the configuration for static
site generation.


# Install static site generator

1. Install Pelican static page generator, see
http://docs.getpelican.com/en/latest/install.html.

On Mac OS, with `Homebrew`:
```bash
brew install python
pip install pelican
pip install markdown
```

2. Install Pelican themes:
```bash
git clone --recursive https://github.com/getpelican/pelican-themes pelican-themes
```


# Generate local site

```bash
make html && make serve
```

If error `ValueError: unknown locale: UTF-8` occurs, consider setting the
following environment variables: `LC_ALL="en_US.UTF-8" LANG="en_US.UTF-8"`.
