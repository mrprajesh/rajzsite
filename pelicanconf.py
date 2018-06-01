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
PLUGINS = ["render_math",'i18n_subsites']

# Blogroll
LINKS = (
		('My Personal Blog', 'http://jeshthink.blogspot.com/'),
         ('My Tech Blog', 'http://mrprajesh.blogspot.com/'),
         ('Theoretical CS Lab', 'http://theory.cse.iitm.ac.in'),
         ('Unique visitors:  <img src="//c.statcounter.com/11617236/0/a2429d81/0/" alt="StatCounter" >', 'http://statcounter.com/'),
('Page hits:   <img src="//c.statcounter.com/11617242/0/19c44117/0/" alt="StatCounter" >', 'http://statcounter.com'),
        )


#~ ('<img src="http://www.reliablecounter.com/count.php?page=cse.iitm.ac.in/~mrprajesh&digit=style/plain/6/&reloads=1" alt="www.reliablecounter.com" title="www.reliablecounter.com" border="0">', 'http://www.reliablecounter.com'),     
        
#<a href="http://www.reliablecounter.com" target="_blank"><img src="http://www.reliablecounter.com/count.php?page=cse.iitm.ac.in/~mrprajesh&digit=style/plain/6/&reloads=1" alt="www.reliablecounter.com" title="www.reliablecounter.com" border="0"></a><br /><a href="http://www.reliablecounter.com/ar/" target="_blank" style="font-family: Geneva, Arial; font-size: 9px; color: #330010; text-decoration: none;"> </a>

# Social widget
SOCIAL = (('Github!', 'https://github.com/mrprajesh'),
		  ('Google Profile', 'https://plus.google.com/u/0/+RajeshPandianM'),
          ('Twitter', 'https://twitter.com/mrprajesh'),
          ('Facebook!', 'https://facebook.com/mrprajesh'),)

DEFAULT_PAGINATION = 10


STATIC_PATHS = ['images', 'pdfs','csvs']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#~ THEME = "notmyidea"
#~ THEME = '/home/rajz/install/pelican-themes/Just-Read'
#~ THEME='/home/rajz/install/pelican-themes/pelican-bootstrap3'
#~ THEME='/home/rajz/install/pelican-themes/built-texts'
#~ THEME='/home/rajz/install/pelican-themes/attilight'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
#MATH_JAX = {'color':'blue','align':'left'}

#~ HEADER_BG_IMG = 'images/header.png'

#~ AUTHORS_BIO = {
  #~ "jd": {
    #~ "fullname": "Rajesh Pandian M",
    #~ "image": "http://www.cse.iitm.ac.in/~mrprajesh/oldWebsite/images/rajesh.jpg",
    #~ "website": "http://www.cse.iitm.ac.in/~mrprajesh",
    #~ "location": "Chennai. India",
    #~ "bio": "I am Rajesh Pandian M"
  #~ }
#~ }
