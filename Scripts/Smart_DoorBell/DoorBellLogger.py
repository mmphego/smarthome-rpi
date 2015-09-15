#!/usr/bin/env python
__author__ = "Mpho Mphego"
__description__ = "Doorbell notifier time logger and email notifier."
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2015/01/10 02:09 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__license__ = "Python"

import time
import datetime
import os
import smtplib
from email.mime.text import MIMEText

#-----------------------Data Logger-----------------
f=open('/home/pi/Logs/DoorBell_Data_Log.txt','a')
now = datetime.datetime.now()
timestamp = now.strftime("%H:%M on %Y/%m/%d")
outstring1 = "Someone was at the door at " + str(timestamp)
outstring2 = "\n********************************************* \n "
outstring = outstring1 + outstring2
f.write(outstring)
f.close()
