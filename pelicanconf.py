#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Refer to [1] for a decent example configuration
# [1] https://github.com/tyleha/beneathdata/blob/master/pelicanconf.py

AUTHOR = 'Chris Mullins'
SITENAME = 'Charleston Python'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/CharlestonPython'),
          ('meetup', 'http://meetup.com/CharlestonPython'),)

GITHUB_URL = 'http://github.com/CharlestonPython'

DEFAULT_PAGINATION = 10

SITELOGO = 'images/Logo_final01.png'
SITELOGO_SIZE = '30'

# Pelican Theme-specific variables
BOOTSTRAP_THEME = 'cosmo'
PYGMENTS_STYLE = 'monokai'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['/home/chris/Projects/Pelican/pelican-plugins']
PLUGINS = ['i18n_subsites']

THEME = '/home/chris/Projects/Pelican/pelican-themes/pelican-bootstrap3'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
