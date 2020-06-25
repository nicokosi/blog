#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolas Kosinski'
SITENAME = "Nicokosi's blog"
SITEURL = 'https://nicokosi.github.io'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

GITHUB_URL = 'http://github.com/nicokosi/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_RSS = None


STATIC_PATHS = [
	'css',
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
  ('linkedin', 'https://www.linkedin.com/in/nicolas-kosinski-95184811'),
  ('rss', 'https://nicokosi.github.io/feeds/all.atom.xml'),
)

DEFAULT_CATEGORY = 'all'
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-clean-blog"
HEADER_COLOR = 'PowderBlue'
SITESUBTITLE = '#SoftwareDevelopment #WhatElse?;-)'
HEADER_TITLE_LOGO = 'images/nicokosi.png'
CSS_OVERRIDE = 'css/nicokosi.css'
FOOTER_INCLUDE = 'custom-footer.html'
IGNORE_FILES = [FOOTER_INCLUDE]
THEME_TEMPLATES_OVERRIDES = ['templates']
