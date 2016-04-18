#Button test
import RPi.GPIO as GPIO
import time

button = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(button)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
