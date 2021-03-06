#!/usr/bin/env python2.7
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.1 $"
__description__ = "Smart Doorbell Notifier with voice and email notification : Interrupt driven"
__date__ = "$Date: 2015/01/11 02:23 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import time
import os
import subprocess
import gc

import RPi.GPIO as GPIO
import push_notification

from logger import LOGGER
from sms_notification import send_sms
from email_notification import send_mail
from pic_notification import take_pic
from yamlConfigFile import configFile

# led = 17 #GPIO0
button = 18  # GPIO1

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
# GPIO.setup(led, GPIO.OUT)
time.sleep(0.1)
# GPIO.output(led, False)

# GPIO 1 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mp3_file =  '/home/pi/Scripts/Smart_DoorBell/DoorNotify.mp3'
mp3_ply = '/usr/bin/mpg123'
play_over_ssh = configFile()['remote_audio_conf']
remote_play = configFile()['remote_play']

def send_all_notifications():
    LOGGER.info('Sending door notifications')
    #    GPIO.output(led, True)
    #with open(os.devnull, 'rb') as devnull:
    if remote_play:
        subprocess.call('cat {} | {}'.format(mp3_file, play_over_ssh), shell=True)
    else:
        subprocess.Popen(mp3_ply + mp3_file,
                         shell=True, stdout=devnull, stderr=devnull).communicate()
    # GPIO.output(led, False)
    take_pic()
    push_notification.send_notifications()
    send_sms()
    send_mail()
    success = False


# define callback functions
# this will run when an event are detected
def buttonHandler(channel):
    if success:
        LOGGER.info("falling edge detected, sending notifications")
        print("falling edge detected, sending notifications")
        send_all_notifications()


try:
    # when a falling edge is detected on port 1, regardless of whatever
    # else is happening in the program, the function buttonHandler will be run
    success = True
    GPIO.add_event_detect(button, GPIO.FALLING, callback=buttonHandler, bouncetime=100)
except:
    LOGGER.exception('Unable to detect falling edge')
    # raise RuntimeError('Unable to detect falling edge')
# finally:
#    GPIO.add_event_detect(button, GPIO.FALLING, callback=buttonHandler, bouncetime=5500)

try:
    LOGGER.info("Waiting for button to be pressed")
    # print "Waiting for falling edge on port {}".format(button)
    while True:
        time.sleep(.25)
except (Exception, KeyboardInterrupt):
    # print '************exiting*********'
    gc.collect()
    GPIO.cleanup()  # clean up GPIO on CTRL+C exit
finally:
    print '************exiting*********'
    LOGGER.debug("Clean up by resetting all GPIO")
    gc.collect()
    GPIO.cleanup()  # clean up GPIO on normal exit
