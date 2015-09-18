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
import logging
from push_notification import send_notification
from sms_notification import send_sms
from email_notification import send_mail

# create logger
LOGGER = logging.getLogger('Doorbell Logger')
LOGGER.setLevel(logging.DEBUG) # log all escalated at and above DEBUG
# add a file handler
fh = logging.FileHandler('Doorbell_Logger.csv')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file

# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)

# add the Handler to the logger
LOGGER.addHandler(fh)

# You can now start issuing logging statements in your code
LOGGER.debug('a debug message')
LOGGER.info('an info message')
LOGGER.warn('A Checkout this warning.')
LOGGER.error('An error writen here.')
LOGGER.critical('Something very critical happened.')
led = 17 #GPIO0
button = 24 #GPIO1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
time.sleep(0.1)
GPIO.output(led, False)

# GPIO 1 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_all_notifications():
    send_notification()
    send_sms()
    send_mail()

# define callback functions
# this will run when an event are detected

def buttonHandler(channel):
    LOGGER.info("falling edge detected on 18")
    GPIO.output(led, True)
    send_all_notifications()
    time.sleep(0.5)
    GPIO.output(led, False)
    os.system("mpg123 /home/pi/Scripts/Smart_DoorBell/DoorNotify.mp3")
    os.system("python /home/pi/Scripts/Smart_DoorBell/DoorBellLogger.py")

# when a falling edge is detected on port 1, regardless of whatever
# else is happening in the program, the function buttonHandler will be run
GPIO.add_event_detect(button, GPIO.FALLING, callback=buttonHandler, bouncetime=5000)

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
