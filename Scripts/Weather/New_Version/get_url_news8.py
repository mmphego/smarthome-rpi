#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.1 $"
__description__ = "News feeder retrieval"
__date__ = "$Date: 2015/01/30 12:47$"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import feedparser

try: 
    rss = feedparser.parse('http://feeds.news24.com/articles/News24/SouthAfrica/rss')
#    newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3]['description'] + '.  ' 
    newsfeed = rss.entries[0]['description'] + "  " + rss.entries[1]['description'] + "  " \
               + rss.entries[2]['description'] + "  " + rss.entries[3]['description'] + "  " \
               + rss.entries[4]['description'] + "  " + rss.entries[5]['description']
#    print newsfeed

# Today's news from News24.com
    news = ' And now, For the latest news around mzansi.  ' + newsfeed

except rss.bozo:
    news = 'Failed to reach News24'
    
print news
