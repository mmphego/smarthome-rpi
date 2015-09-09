#!/usr/bin/env python2.7
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.0 $"
__description__ = "Closet Door sensor for warning against Rain : Interrupt driven"
__date__ = "$Date: 2015/01/14 01:59 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import RPi.GPIO as GPIO
import time
import os

# led = 22 #GPIO0
button = 18 #GPIO1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# GPIO.setup(led, GPIO.OUT)
time.sleep(0.1)
# GPIO.output(led, False)

# GPIO 1 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# define callback functions
# this will run when an event are detected
def buttonHandler(channel):
    print "Rising edge detected on 18"
    os.system("python /home/pi/Scripts/ClosetDoorWarning/weatherWarning.py")
    # GPIO.output(led, True)
    time.sleep(0.1)
    # GPIO.output(led, False)

# when a falling edge is detected on port 1, regardless of whatever
# else is happening in the program, the function buttonHandler will be run
GPIO.add_event_detect(button, GPIO.RISING , callback=buttonHandler, bouncetime=5000)

try:
    print "Waiting for button to be pressed"
    while True:
        time.sleep(10)
        continue
except:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
finally :
    GPIO.cleanup()           # clean up GPIO on normal exit
    print "Clean up by resetting all GPIO"
