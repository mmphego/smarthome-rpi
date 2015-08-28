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
try:
    from gtts import gTTS
except ImportError:
    import pip
    pip.main(['install', 'gTTS'])

coffeemaker = 4 #GPIO0
count = 1

# end
end = ' Thats all for now. Have a nice day. Good bye!'

"""
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
time.sleep(0.1)
GPIO.setup(coffeemaker, GPIO.OUT)
time.sleep(0.1)
"""

# Turn all of the parts into a single string
words = (gmt + day + wtr + frc + news + end)
# strip any quotation marks
words = words.replace('"', '').strip().split('. ')

try:
    for i,line in enumerate(words):
        tts = gTTS(text=line, lang='en')
        tts.save('{}.mp3'.format(i))
    # Play the mp3s returned
    [subprocess.call ('mpg123 {}.mp3'.format(mp3_file), shell=True)
                        for mp3_file in range(i)]

# festival is now called in case of error reaching Google
except subprocess.CalledProcessError:
    subprocess.check_output("echo " + words + " | festival --tts ", shell=True)

# Cleanup any mp3 files created in this directory.
subprocess.call ('sudo rm *.mp3', shell=True)
"""
# Enabling GPIO for relay switch to turn on coffee maker
GPIO.output(coffeemaker, True)
# Time can be dependent on the make and model of the coffee maker.
time.sleep(600)
GPIO.output(coffeemaker, False)
"""
