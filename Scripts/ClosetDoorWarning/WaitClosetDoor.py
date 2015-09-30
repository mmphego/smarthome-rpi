#!/usr/bin/env python2.7
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.2 $"
__description__ = "Closet Door sensor for warning against Rain : Interrupt driven"
__date__ = "$Date: 2015/01/14 01:59 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import RPi.GPIO as GPIO
import time
import weatherWarning
from logger import LOGGER

#led = 22 #GPIO0
button = 18 #GPIO1

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
# GPIO.setup(led, GPIO.OUT)
# time.sleep(0.1)
# GPIO.output(led, False)

# GPIO 1 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# define callback functions
# this will run when an event are detected
def get_notification():
    # GPIO.output(led, True)
    weatherWarning.notification()
    # GPIO.output(led, False)
    LOGGER.info('Weather updated and user notified')

def buttonHandler(channel):
    LOGGER.info("Closet Door opened")
    get_notification()

# when a falling edge is detected on port 1, regardless of whatever
# else is happening in the program, the function buttonHandler will be run
GPIO.add_event_detect(button, GPIO.RISING , callback=buttonHandler, bouncetime=5000)

try:
    while True:
        time.sleep(10)
        continue
except Exception:
    raise RuntimeError('Error occured')
LOGGER.info('clean up GPIO on normal exit')
GPIO.cleanup()           # clean up GPIO on normal exit
