#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.3 $"
__description__ = "Voice enabled Smart Alarm with weather, news and coffee notifier"
__date__ = "$Date: 2015/01/31 14:55 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import subprocess
import time
import feedparser
#import RPi.GPIO as GPIO
from better_spoken_time3 import gmt, day
from get_url_weather9 import wtr, frc
from get_url_news8 import news
from yamlConfigFile import configFile

try:
    import gtts
except ImportError:
    import pip
    pip.main(['install', 'gTTS'])
finally:
    from gtts import gTTS
#coffeemaker = 4 #GPIO0
end = 'That is all for now Have a nice day.'
# url = 'http://feeds.feedburner.com/brainyquote/QUOTEBR'
url_quote = 'https://www.quotesdaddy.com/feed/tagged/Inspirational'
rss = feedparser.parse(url_quote)

play_over_ssh = configFile()['remote_audio_conf']
remote_play = configFile()['remote_play']

mp3_playr = '/usr/bin/mpg123'
morning_alarm = '/home/pi/Scripts/Smart_Alarm/morning_alarm.mp3'

#GPIO.setwarnings(True)
#GPIO.setmode(GPIO.BCM)
#time.sleep(0.01)
#GPIO.setup(coffeemaker, GPIO.OUT)
#time.sleep(0.01)
# Turn all of the parts into a single string

if rss['status'] == 200:
    try:
        quote = '. And todays quote ' + str(rss['entries'][0]['summary']).replace('-', '')
    except:
        quote = '. And todays quote ' + str(rss['entries'][0]['summary'])
else:
    quote = 'No quote today'

try:
    words = str(gmt + day + wtr + frc + news + quote + end)
except UnicodeEncodeError:
    words = str(gmt + day + wtr + frc + news.encode('ascii', 'ignore') + quote + end)
# strip any quotation marks
words = words.replace('"', '').strip().split('. ')

try:
    for i,line in enumerate(words):
        tts = gTTS(text=line, lang='en-us')
        tts.save('{}.mp3'.format(i))
except:
    subprocess.check_output("echo " + words + " | festival --tts ", shell=True)
    # Play the mp3s returned
try:
    if remote_play:
        subprocess.call('cat {} | {}'.format(morning_alarm, play_over_ssh), shell=True)
        for mp3_file in xrange(len(words)):
            subprocess.call ('cat {}.mp3 | {}'.format(mp3_file, play_over_ssh), shell=True)
            subprocess.call ('rm {}.mp3'.format(mp3_file), shell=True)
    else:
        subprocess.call('{} {}'.format(mp3_playr, morning_alarm), shell=True)
        for mp3_file in xrange(len(words)):
            subprocess.call('{} {}.mp3 '.format(mp3_playr, mp3_file), shell=True)

# festival is now called in case of error reaching Google
except subprocess.CalledProcessError:
    subprocess.check_output("echo " + words + " | festival --tts ", shell=True)

# Cleanup any mp3 files created in this directory.


# Enabling GPIO for relay switch to turn on coffee maker
#GPIO.output(coffeemaker, True)
# Time can be dependent on the make and model of the coffee maker.
#time.sleep(600)
#GPIO.output(coffeemaker, False)
