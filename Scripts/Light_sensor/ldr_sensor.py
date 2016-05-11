#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

from numpy import average

class LDR(object):
    def __init__(self):
        self.sampler = 3
        self.LDRPin = 16
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LDRPin, GPIO.OUT)

        GPIO.output(self.LDRPin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(self.LDRPin, GPIO.IN)

    def RCtime(self):
        value = 0
        # Measure timing using LDRPin
        while (GPIO.input(LDRPin) == GPIO.TRUE):
            # Count loops until voltage across
            # capacitor reads high on GPIO
            value += 1
        samples = []
        for i in xrange(self.sampler):
            samples.append(value)
        return  average(samples)

get_ldr = LDR()

while True:
    print get_ldr.RCtime()
