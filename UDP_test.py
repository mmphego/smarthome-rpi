#!/usr/bin/python2
import RPi.GPIO as GPIO
import time
import os
import socket


led = 26 #GPIO0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
time.sleep(0.1)
GPIO.output(led, False)
time.sleep(1)
GPIO.output(led, True)
time.sleep(1)
GPIO.output(led, False)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
UDP_IP = s.getsockname()[0]
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
print "UDP Ready to Receive!"
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    if data == "1" or data == "one" :
        GPIO.output(led, True)

    elif data == "2" or data == "two" :
        GPIO.output(led, False)
    else :
        print "invalid parameter"

    time.sleep(1)
   # GPIO.cleanup()
#    break
    #continue
