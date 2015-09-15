#!/usr/bin/env python
__author__ = "Mpho Mphego"
__description__ =
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__license__ = "Python"


import smtplib
import datetime
from email.mime.text import MIMEText

USERNAME = "homeauto112@gmail.com"
PASSWORD = "Livhuwani$12"
MAILTO  = "mpho112@gmail.com"

def send_mail():
    print "Sending Email Notification"
    msg = MIMEText('Someone was at the door at {}'.format(today.strftime('%b %d %Y')))
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
