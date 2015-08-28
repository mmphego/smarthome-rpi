#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.2 $"
__description__ = "News feeder retrieval"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import feedparser

# Today's news from News24.com
try:
    rss = feedparser.parse('http://feeds.news24.com/articles/News24/SouthAfrica/rss')
    newsfeed = (rss.entries[0]['description'] + "\n" + rss.entries[1]['description']
        + "\n" + rss.entries[2]['description'] + "\n" + rss.entries[3]['description']
            + "\n" + rss.entries[4]['description'] + "\n" + rss.entries[5]['description'])

    news = ' And now, For the latest news around mzansi.  ' + newsfeed

except rss.bozo:
    news = 'Failed to reach News24'
