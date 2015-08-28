#!/usr/bin/python
__author__ = "Mpho Mphego"
__description__ = "Raspberry Pi I2C Arduino: Temperature Data Logger"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2015/01/05 14:43 $"
__url__ = "mpho112.wordpress.com"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__license__ = "Python"

#import smbus
import time
import datetime
#import csv

while True:
    fh=open("/home/pi/Logs/indoorTemp.txt")
    for line in fh:
        number = line.rstrip()
    f=open('/home/pi/Logs/Temp_Data_Log.txt','a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d     %H:%M")
    outvalue = number
#    degree =  u'\N{DEGREE SIGN}'#unichr(176).encode("latin-1")
#    print degree
    outstring = str(timestamp) + "    " + str(outvalue) + " C" "\n"
#    print outstring
    f.write(outstring)
    f.close()
    time.sleep(60)
