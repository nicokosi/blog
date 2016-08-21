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

STATIC_PATHS = [
	'images',
	'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
  ('twitter', 'http://twitter.com/nicokosi'),
  ('github', 'http://github.com/nicokosi'),
)

DEFAULT_CATEGORY = 'all'
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pelican-clean-blog"
#HEADER_COVER = 'images/nicokosi-large.png'
HEADER_COLOR = 'PowderBlue'
SITESUBTITLE = '#SoftwareDevelopment #Tools #ProgrammingLanguages #WhatElse?;-)'
