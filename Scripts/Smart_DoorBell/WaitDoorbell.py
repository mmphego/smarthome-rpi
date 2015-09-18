#!/usr/bin/env python2.7
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.1 $"
__description__ = "Smart Doorbell Notifier with voice and email notification : Interrupt driven"
__date__ = "$Date: 2015/01/11 02:23 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import RPi.GPIO as GPIO
import time
import os
from logger import LOGGER
from push_notification import send_notification
from sms_notification import send_sms
from email_notification import send_mail

led = 17 #GPIO0
button = 24 #GPIO1

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
time.sleep(0.1)
GPIO.output(led, False)

# GPIO 1 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_all_notifications():
    LOGGER.info('Sending door notifications')
    GPIO.output(led, True)
    send_notification()
    send_sms()
    send_mail()
    time.sleep(0.5)
    GPIO.output(led, False)
    os.system("mpg123 /home/pi/Scripts/Smart_DoorBell/DoorNotify.mp3")

# define callback functions
# this will run when an event are detected
def buttonHandler(channel):
    LOGGER.debug("falling edge detected, sending notifications")
    send_all_notifications()

try:
    # when a falling edge is detected on port 1, regardless of whatever
    # else is happening in the program, the function buttonHandler will be run
    GPIO.add_event_detect(button, GPIO.FALLING, callback=buttonHandler, bouncetime=5000)
except Exception:
    LOGGER.error('Unable to detect falling edge')
    raise RuntimeError('Unable to detect falling edge')

try:
    LOGGER.debug("Waiting for button to be pressed")
    while True:
        time.sleep(10)
        continue
except Exception:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
finally:
    LOGGER.debug("Clean up by resetting all GPIO")
    GPIO.cleanup()           # clean up GPIO on normal exit
