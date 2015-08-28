#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.2 $"
__description__ = "Voice enabled Smart Alarm with weather, news and coffee notifier"
__date__ = "$Date: 2015/01/31 14:55 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import subprocess
import time
import os
#import RPi.GPIO as GPIO
import textwrap
from better_spoken_time3 import gmt, day
from get_url_weather9 import wtr, frc
from get_url_news8 import news

coffeemaker = 4 #GPIO0
count = 1
# your name goes here:
name = ''
# key to getting text to speech
head = 'wget -q -U Mozilla '
tail = '.mp3 '
# end
end = ' Thats all for now.  Have a nice day.  '
##################################################
"""
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
time.sleep(0.1)
GPIO.setup(coffeemaker, GPIO.OUT)
time.sleep(0.1)
"""

# Turn all of the parts into a single string
#wad = (gmt + name + day + wtr + end)
#wad = (gmt + name + day + wtr + frc + btc + stck + news + end)
wad = (gmt + name + day + wtr + frc + news + end)
print wad

# strip any quotation marks
wad = wad.replace('"', '').strip()
wad = wad.replace("'", '').strip()

# If you want to say with pure FOSS projects, use festival instead of google tts by uncommenting out the line below AND commenting out EVERYTHING else
# print subprocess.check_output("echo " + wad + " | festival --tts ", shell=True)

# Google voice only accepts 100 characters or less, so split into chunks
shorts = []
for chunk in wad.split('. '):
#for chunk in wad.split('.  '):
    shorts.extend(textwrap.wrap(chunk, 100))
print shorts


# Send shorts to Google and return mp3s
try:
  for sentence in shorts:
# UK Female Voice
    sendthis = sentence.join(['"http://translate.google.com/translate_tts?tl=en&q=', '" -O ~/'])
#    sendthis = sentence.join(['"http://translate.google.com/translate_tts?tl=en&q=', '" -O /mnt/ram/'])
# US Female Voice
#    sendthis = sentence.join(['"http://translate.google.com/translate_tts?&tl=en-US&ie=UTF-8&q=', '" -O /mnt/ram/'])
    print(head + sendthis + str(count).zfill(2) + str(tail))
    print subprocess.check_output (head + sendthis + str(count).zfill(2) + str(tail), shell=True)
    count = count + 1


# Play the mp3s returned
#  print subprocess.call ('mpg123 -h 10 -d 11 /mnt/ram/*.mp3', shell=True)
  print subprocess.call ('mpg123 -h 10 -d 11 /tmp/*.mp3', shell=True)

# festival is now called in case of error reaching Google
except subprocess.CalledProcessError:
  print subprocess.check_output("echo " + wad + " | festival --tts ", shell=True)

# Cleanup any mp3 files created in this directory.
print 'cleaning up now'
#print subprocess.call ('sudo rm /mnt/ram/*.mp3', shell=True)
#print subprocess.call ('sudo rm /home/pi/Scripts/Weather/New_Version/*.pyc', shell=True)
#Run Get weather bash script
#os.system("bash /home/pi/Scripts/Weather/Get_weather.sh")

# Enabling GPIO for relay switch to turn on coffee maker
#GPIO.output(coffeemaker, True)
# Time can be dependent on the make and model of the coffee maker.
time.sleep(600)
#GPIO.output(coffeemaker, False)
