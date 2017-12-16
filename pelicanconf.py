#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import re, os

# Local:
SITEURL = ''

## Github Pages:
#SITEURL = 'experimental-design'


AUTHOR = u'charlesreid1'
SITENAME = u'experimental-design'

PATH = 'content'
THEME = 'cmr-2017-theme'

# to install this theme:
# git checkout http://charlesreid1.com:3000/charlesreid1/cmr-2017-theme
# pelican-themes -i cmr-2017-theme


OUTPUT_PATH = 'docs/'



# -------------------
# Plugins:
HOME = os.environ.get('HOME')
PLUGIN_PATHS = [HOME+'/codes/pelican-plugins/']
PLUGINS = ['render_math']

#MARKUP = ('md')

### # Don't try to turn HTML files into pages
### READERS = {'html': None}


# --------------------
# Static content

STATIC_PATHS = ['images']



# --------------------
# Templates

######################
# Templates:

EXTRA_TEMPLATES_PATHS = []
TEMPLATE_PAGES = {}

## To add paths:
#EXTRA_TEMPLATES_PATHS.append('notebooks')

## To add template pages in those directories:
#TEMPLATE_PAGES['mynotebook.html'] = 'mynotebook.html'




# --------------8<---------------------

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

