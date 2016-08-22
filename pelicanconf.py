#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolas Kosinski'
SITENAME = "Nicokosi's blog"
SITEURL = 'http://nicokosi.github.io'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

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
HEADER_COLOR = 'PowderBlue'
SITESUBTITLE = '#SoftwareDevelopment #WhatElse?;-)'
HEADER_TITLE_LOGO = 'images/nicokosi.png'

DISQUS_SITENAME = 'nicokosi-blog'
