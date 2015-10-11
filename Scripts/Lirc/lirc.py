import lirc
import time
import RPi.GPIO as GPIO
print "Setting up GPIO"
LED_PIN = 17 #ledje aanzetten
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, True)


sockid = lirc.init("rcled", blocking=False)
while True:
try:
button = lirc.nextcode()
print("Press RC button , die geconfigureerd staat in etc/lirc/lircrc!")
GPIO.output(LED_PIN, True)
if len(button) == 0: continue
print(button[0])
print (len(button))
GPIO.output(LED_PIN, False)

time.sleep(1)
except KeyboardInterrupt:
lirc.deinit()
break


#file : etc/lirc/lircrc
#begin
# button = KEY_0
# prog = rcled
# config = echo "Hello knop nul, via etc-lirc-lircrc"
#end
#begin
# button = KEY_0
# prog = irexec
# config = echo "Hello knop nul"
#end

# Please make this file available to others
# by sending it to <lirc@bartelmus.de>
#
# this config file was automatically generated
# using lirc-0.9.0-pre1(default) on Wed Oct 8 23:54:32 2014
#
# contributed by
#
# brand: /home/pi/lircd.conf
# model no. of remote control:
# devices being controlled by this remote:
#


#file : etc/lirc/lircd.conf : dit bestandje word gemaakt door aan te leren van knoppen van de rc
# via een soort wizard moet je een geregistreerde toets invullen , en dan de code aanleren
#begin remote
#
# name /home/pi/lircd.conf
# bits 16
# flags SPACE_ENC|CONST_LENGTH
# eps 30
# aeps 100
#
# header 9052 4509
# one 564 1693
# zero 564 567
# ptrail 571
# repeat 9056 2250
# pre_data_bits 16
# pre_data 0x20D3
# gap 108478
# toggle_bit_mask 0x0
#
# begin codes
# KEY_0 0xD827
# KEY_1 0x827D
# end codes
#
#end remote
