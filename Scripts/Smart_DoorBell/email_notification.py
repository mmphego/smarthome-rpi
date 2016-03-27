#!/usr/bin/env python
__author__ = "Mpho Mphego"
__description__ = "Real-time notifications on your Android mobile"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__license__ = "Python"

import os
import smtplib
from time import strftime
from logger import LOGGER
from pic_notification import take_pic
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


USERNAME = "homeauto112@gmail.com"
PASSWORD = "Livhuwani$12"
MAILTO  = "mpho112@gmail.com"
SUB = 'Doorbell notification!'
MESSAGE = 'Someone was at the door at {}'.format(strftime('%b %d %Y'))
FILE = 'image.jpg'

def send_mail():
    LOGGER.info ("Sending Email Notification")
    take_pic()

    msg = MIMEMultipart()

    msg['From'] = USERNAME
    msg['To'] = MAILTO
    msg['Subject'] = SUB

    msg.attach(MIMEText(MESSAGE))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(FILE, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(FILE))
    msg.attach(part)
    try:
        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(USERNAME, PASSWORD)
        mailServer.sendmail(USERNAME, MAILTO, msg.as_string())
        # Should be mailServer.quit(), but that crashes...
    except Exception as e:
        LOGGER.error ("Failed to connect to email server: Error: {}".format(e))
        raise RuntimeError("Failed to connect to email server: Error: {}".format(e))
    finally:
        mailServer.close()
