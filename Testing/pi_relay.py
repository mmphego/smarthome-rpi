import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
relay1 = 5
relay2 = 6
relay3 = 17
relay4 = 27

# Set relay pins as output
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)

while (True):
    
    # Turn all relays ON
    GPIO.output(relay1, GPIO.HIGH)
    GPIO.output(relay2, GPIO.HIGH)
    GPIO.output(relay3, GPIO.HIGH)
    GPIO.output(relay4, GPIO.HIGH)
    # Sleep for 2 seconds
    sleep(2) 
    # Turn all relays OFF
    GPIO.output(relay1, GPIO.LOW)
    GPIO.output(relay2, GPIO.LOW)
    GPIO.output(relay3, GPIO.LOW)
    GPIO.output(relay4, GPIO.LOW)
    # Sleep for 2 seconds
    sleep(2)
