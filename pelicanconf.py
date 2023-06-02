#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rajesh Pandian M'
SITENAME = u'Rajesh Pandian M'
SITESUBTITLE= u''
# ~ SITEURL = 'https://mrprajesh.co.in'

PATH = 'content'

DEFAULT_DATE_FORMAT = '%d-%b-%Y'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

##
PAGE_ORDER_BY = 'page-order'

# It works only with the internet connection
PLUGIN_PATHS = ['/home/rajesh/install/pelican-plugins']
PLUGINS = ["render_math",'i18n_subsites']

# Blogroll
LINKS = (
         ('MyTeach Encounters', 'https://mrprajesh.co.in/blog'),
         ('My Personal Blog', 'http://jeshthink.blogspot.com/'),
         ('My old Tech Blog', 'http://mrprajesh.blogspot.com/'),
         ('Theoretical CS Lab', 'http://theory.cse.iitm.ac.in'),
         ('Unique visitors:  <img src="//c.statcounter.com/11617236/0/a2429d81/0/" alt="StatCounter" >', 'http://statcounter.com/'),
('Page hits:   <img src="//c.statcounter.com/11617242/0/19c44117/0/" alt="StatCounter" >', 'http://statcounter.com'),
		  ('TeachForTN', 'https://yclaacademy.github.io'),
         # ~ (' Channel for School', 'https://www.youtube.com/channel/UC7AYCv3SJotZtyfNuT_UBqA/about'),
         # ~ (' Channel for College', 'https://www.youtube.com/YCLAAcademy/about'),
        )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/mrprajesh'),
          ('ORCHID', 'https://orcid.org/0000-0003-4702-4678'),
          ('Twitter', 'https://twitter.com/mrprajesh'),
          ('DBLB', 'https://dblp.org/pid/313/1579.html'),
          ('Google Scholar', 'https://scholar.google.com/citations?user=onuO9hYAAAAJ'),
          ('Linkedin', 'https://www.linkedin.com/in/rajesh-pandian-muniasamy-524717a/'),
          ('Facebook', 'https://facebook.com/mrprajesh'),
          )

TWITTER_USERNAME='mrprajesh'
GITHUB_USERNAME='mrprajesh'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs','csvs']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# ~ THEME = "notmyidea"
THEME = '/home/rajesh/gitSites/notmyidea-cms-mine'
#USE_FOLDER_AS_CATEGORY=True
#~ THEME = '/home/rajz/install/pelican-themes/Just-Read'
#~ THEME='/home/rajz/install/pelican-themes/pelican-bootstrap3'
#~ THEME='/home/rajz/install/pelican-themes/built-texts'
#~ THEME='/home/rajz/install/pelican-themes/attilight'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {}, #'css_class': 'highlight'
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
		'title': 'Contents',
		'anchorlink': True,
        },
    },
    'output_format': 'html5',
}
