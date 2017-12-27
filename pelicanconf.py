#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rajesh Pandian M'
SITENAME = u'Rajesh Pandian M'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

##
PAGE_ORDER_BY = 'page-order'

# It works only with the internet connection
PLUGIN_PATHS = ['/home/rajz/install/pelican-plugins']
PLUGINS = ["render_math"]

# Blogroll
LINKS = (('My Personal Blog', 'http://jeshthink.blogspot.com/'),
         ('My Tech Blog', 'http://mrprajesh.blogspot.com/'),
         ('The views expressed here are MINE and do not represent those of the institutions that I work with/at in any way.', '#'),)

# Social widget
SOCIAL = (('Github!', 'https://github.com/mrprajesh'),
		  ('Google Profile', 'https://plus.google.com/u/0/+RajeshPandianM'),
          ('Twitter', 'https://twitter.com/mrprajesh'),
          ('Facebook!', 'https://facebook.com/mrprajesh'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "notmyidea"
#THEME = '/home/rajz/install/pelican-themes/Just-Read'
#THEME = '/home/rajz/install/pelican-themes/apricot'
