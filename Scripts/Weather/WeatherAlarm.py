#!/usr/bin/env python2.7
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.0 $"
__description__ = "Alarm and weather notifier"
__date__ = "$Date: 2015/01/14 01:59 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import os
if os.system("ping -c 1 www.google.com >> /dev/null") == 0:
	print "Internet available"
	os.system("bash /home/pi/Scripts/Weather/Get_weather.sh")
else:
	os.system("aplay /home/pi/Scripts/Weather/noInternet.wav")    
