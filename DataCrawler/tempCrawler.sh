#!/bin/bash
#__author__ = "Mpho Mphego"
#__version__ = "$Revision: 1.1 $"
#__date__ = "$Date: 2015/01/09 11:24 $"
#__url__ = "mpho112.wordpress.com"
#__copyright__ = "Copyright (c) 2014 Mpho Mphego"
#__license__ = "Bash"

# Purpose of this script is to retrieve data from Arduino via I2C and then display it on graphite.
# Also retrieve additional information such as RPi internal Temp 

while :
do
echo "Retrieving Data at"  `date`
echo "rpi.data.roomTemp" `home_auto 7 | grep Received | awk '{ print $2}'` `date +%s` | nc -q0 127.0.0.1 2003
sleep 0.5s
echo "rpi.data.internalTemp" `home_auto 6 | grep Received | awk '{ print $2}'` `date +%s` | nc -q0 127.0.0.1 2003
sleep 0.5s
echo "rpi.data.internalRPiTemp" `vcgencmd measure_temp | egrep "[0-9.]{4,}" -o` `date +%s` | nc -q0 127.0.0.1 2003
#home_auto 7 | grep Received | awk '{ print $2}' > ~/indoorTemp.txt
echo "Data Sent at" `date` 
echo "<--------------------------------->"
sleep 70s
done
