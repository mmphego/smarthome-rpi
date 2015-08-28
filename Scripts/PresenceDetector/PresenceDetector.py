#!/usr/bin/python2
# Purpose of this script is to ping a certain static IP(android mobile) is destination is
# reachable set a  gpio pin and activate flite(voice response) else if it not detected
# gpio will remain off
# Created by Mpho Mphego (mpho112@gmail.com)
# http://pastebin.com/nLkaZ308

# Import the libraries to use time delays, send os commands and access GPIO pins
#import RPi.GPIO as GPIO #module requires root privilages
# Decided to use WiringPi packages
import time
import os
# LED on ping 7 header, GPIO07
os.system("gpio mode 7 out")
#GPIO.setmode(GPIO.BOARD) # Set pin numbering to board numbering
#GPIO.setup(4, GPIO.OUT) # Setup pin 7 as an input
count = 0
while True: # Setup a while loop to wait for a button press
    if os.system("ping -c 1 172.18.20.209 > /dev/null 2>&1") == 0:# Send command to os
        print "host is detected"
#        time.sleep(1)
        time.sleep(1)
#        os.system('flite -t "Welcome Home Pau"')
	os.system('mpg123 Welcome_Home.mp3')
        time.sleep(2)
#        os.system("gpio write 7 0")
        os.system('sudo service cellDetect stop')
        break

    else:
        print "host unreachable"
        os.system("gpio write 7 0")

    break
time.sleep(60) # Allow a sleep time of 1 second to reduce CPU usage

