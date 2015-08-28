#!/bin/bash
#__author__ = "Mpho Mphego"
#__description__ = "Receive Indoor Temp to file"
#__version__ = "$Revision: 1.0 $"
#__date__ = "$Date: 2015/01/04 00:14 $"
#__url__ = "mpho112.wordpress.com"
#__copyright__ = "Copyright (c) 2015 Mpho Mphego"
#__license__ = "Python"

while :
do
home_auto 7 | grep Received | awk '{ print $2}' > /home/pi/Logs/indoorTemp.txt
sleep 1m
done
