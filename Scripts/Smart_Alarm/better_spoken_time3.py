#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.2 $"
__description__ = "Better Time"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import time
from yamlConfigFile import configFile

if int(time.strftime("%d")) == 1:  suffixed = 'first'
if int(time.strftime("%d")) == 2:  suffixed = 'second'
if int(time.strftime("%d")) == 3:  suffixed = 'third'
if int(time.strftime("%d")) == 4:  suffixed = 'fourth'
if int(time.strftime("%d")) == 5:  suffixed = 'fifth'
if int(time.strftime("%d")) == 6:  suffixed = 'sixth'
if int(time.strftime("%d")) == 7:  suffixed = 'seventh'
if int(time.strftime("%d")) == 8:  suffixed = 'eighth'
if int(time.strftime("%d")) == 9:  suffixed = 'ninth'
if int(time.strftime("%d")) == 10:  suffixed = 'tenth'
if int(time.strftime("%d")) == 11:  suffixed = 'eleventh'
if int(time.strftime("%d")) == 12:  suffixed = 'twelfth'
if int(time.strftime("%d")) == 13:  suffixed = 'thirteenth'
if int(time.strftime("%d")) == 14:  suffixed = 'fouteenth'
if int(time.strftime("%d")) == 15:  suffixed = 'fifteenth'
if int(time.strftime("%d")) == 16:  suffixed = 'sixteenth'
if int(time.strftime("%d")) == 17:  suffixed = 'seventeeth'
if int(time.strftime("%d")) == 18:  suffixed = 'eighteenth'
if int(time.strftime("%d")) == 19:  suffixed = 'nineteenth'
if int(time.strftime("%d")) == 20:  suffixed = 'twentieth'
if int(time.strftime("%d")) == 21:  suffixed = 'twentyfirst'
if int(time.strftime("%d")) == 22:  suffixed = 'twentysecond'
if int(time.strftime("%d")) == 23:  suffixed = 'twentythird'
if int(time.strftime("%d")) == 24:  suffixed = 'twentyfourth'
if int(time.strftime("%d")) == 25:  suffixed = 'twentyfifth'
if int(time.strftime("%d")) == 26:  suffixed = 'twentysixth'
if int(time.strftime("%d")) == 27:  suffixed = 'twentyseventh'
if int(time.strftime("%d")) == 28:  suffixed = 'twentyeigth'
if int(time.strftime("%d")) == 29:  suffixed = 'twentyninth'
if int(time.strftime("%d")) == 30:  suffixed = 'thirtieth'
if int(time.strftime("%d")) == 31:  suffixed = 'thirtyfirst'

now = (time.strftime("%A %B") + " the " + suffixed + ','
    + time.strftime(" %I %M %p"))

if int(time.strftime("%H")) < 12:  period = 'morning'
if int(time.strftime("%H")) >= 12:  period = 'afternoon'
if int(time.strftime("%H")) >= 17:  period = 'evening'

# reads out good morning + my name
user = configFile()['username']
gmt = ('Good ' + period + ', {}!'.format(user) + 'It is time to wakeup, '
    'I am preparing coffee it should be ready in 10 minutes.')
day = " it's " + now + ". "
