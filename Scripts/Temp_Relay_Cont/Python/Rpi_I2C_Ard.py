#!/usr/bin/python
__author__ = "Mpho Mphego"
__description__ = "Raspberry Pi(master) I2C Arduino(slave) [setup]"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2014/12/15 18:23 $"
__url__ = "mpho112.wordpress.com"
__copyright__ = "Copyright (c) 2014 Mpho Mphego"
__license__ = "Python"
# Update:
#   1.1 : removed while loop
#   1.2 : Updated script, included arguments parsing directly from cli without the need of key input.
import smbus
import time
import sys
import serial

#print 'Number of arguments:', len(sys.argv), 'arguments.'

BAUD = 9600
try:
    serial_com = serial.Serial('/dev/ttyACM0', BAUD)
except serial.SerialException:
    serial_com = serial.Serial('/dev/ttyACM1', BAUD)

## for RPI version 1, use "bus = smbus.SMBus(0)"
#bus = smbus.SMBus(1)
## This is the address we setup in the Arduino Program
#address = 0x04

#def writeNumber(value):
    #bus.write_byte(address, value)
    #time.sleep(0.1)
    #return -1
##    return int(value)

#def readNumber():
    #number = bus.read_byte(address)
    #time.sleep(0.1)
    #return int(number)

#while True:
time.sleep(0.1)
#var = input("Enter 1 - 9: ")
print ("parsed argument: %s" % str(sys.argv[1]))
var = int(sys.argv[1])
#print type(int(a))
#var = a
if not var:
    print "Please Enter 1 - 9"
#    continue
time.sleep(0.1)
#writeNumber(var)
serial_com.write(var)

print "RPI: Hi Arduino, I sent you ", var
# sleep one second
time.sleep(0.1)

received_data = serial_com.readline()
print "Arduino: Hey RPI, I received a digit ", received_data
