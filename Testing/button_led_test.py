# Button and LED test
import RPi.GPIO as GPIO
import time

button = 18
led = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)

while True:
    input_state = GPIO.input(button)
    GPIO.output(led, False)

    if input_state == False:
        print('Button Pressed')
        GPIO.output(led, True)
        time.sleep(0.2)
GPIO.cleanup()           # clean up GPIO on normal exit
