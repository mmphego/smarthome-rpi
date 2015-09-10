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

# -----------------------Email Notifier----------------------
USERNAME = "homeauto112@gmail.com"
PASSWORD = "Livhuwani$12"
MAILTO  = "mpho112@gmail.com"

if os.system("ping -c 1 www.google.com >> /dev/null 2&>1") == 0 :
    print "Sending Email Notification"
    msg = MIMEText('Someone is ringing the doorbell! \nGo Check!')
    msg['Subject'] = 'Doorbell notification!'
    msg['From'] = USERNAME
    msg['To'] = MAILTO

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME, MAILTO, msg.as_string())
    server.quit()
else:
    print "Unable to connect to Internet."
