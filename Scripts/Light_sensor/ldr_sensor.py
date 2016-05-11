#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os
from numpy import average

GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    samples = []
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
        samples.append(reading)
    return average(samples)/10.

def cleanup():
    GPIO.cleanup()
