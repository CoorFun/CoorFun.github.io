#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Coor'
SITENAME = u"CoorFang's Blog"
SITESUBTITLE = u"Graduate @ ISEP/ Hardwear Engineer"
SITEURL = ' https://coorfun.com'
TIMEZONE = 'Europe/Paris'

#RELATIVE_URLS = True

GITHUB_URL = 'https://github.com/CoorFun/'

#Source directory, output directory and theme directory
OUTPUT_PATH = '/Users/Coor/Sites/CoorFun.github.io'
PATH = '/Users/Coor/Google Drive/Blogs'
THEME = '/Users/Coor/Sites/Pelican-Customize-Theme'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Misc'
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
#LINKS = (('ABOUT ME', 'http://coorfun.com/about.html'),
#         ('CV', 'http://coorfun.com/cv.pdf'),
#         ('简体中文', 'http://coorfun.com/'))

# Social widget
SOCIAL = (('github', 'https://github.com/CoorFun/'),
          ('weibo', 'http://weibo.com/1847796960/'),
          ('instagram', 'https://www.instagram.com/coorfang/'))

DEFAULT_PAGINATION = 100


ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "coorfangs-blog"
