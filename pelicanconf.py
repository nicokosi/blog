#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolas Kosinski'
SITENAME = "Nicokosi's blog"
SITEURL = 'http://nicokosi.github.io'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

GITHUB_URL = 'http://github.com/nicokosi/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "pelican-themes/hyde"

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
  ('twitter', 'http://twitter.com/nicokosi'),
  ('github', 'http://github.com/nicokosi'),
)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme configuration:
ABOUT_IMAGE = "images/nicokosi.png"
