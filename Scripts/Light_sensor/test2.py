import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 16
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
    print "Motion Detected!"

time.sleep(2)

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while True:
        time.sleep(100)
except:
    pass

finally:
    GPIO.cleanup()

