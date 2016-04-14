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

serial_com.close()
time.sleep(0.2)
serial_com.open()
time.sleep(0.2)
var = str(sys.argv[1])
time.sleep(0.2)
serial_com.write(var)
time.sleep(0.1)

#print ("parsed argument: %s" % str(sys.argv[1]))
#var = str(sys.argv[1])

#if not var:
#    print "Please Enter 1 - 9"
#time.sleep(0.5)

#import IPython;IPython.embed()
#serial_com.write(var)

#print "RPI: Hi Arduino, I sent you ", var
# sleep one second
#time.sleep(0.1)

#received_data = serial_com.readline()
#print "Arduino: Hey RPI, I received a digit ", received_data
