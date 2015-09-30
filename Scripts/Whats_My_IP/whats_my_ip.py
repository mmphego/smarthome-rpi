#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.2 $"
__description__ = "Finds IP on startup and email the user"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import urllib2
import time
from logger import LOGGER

# Include button for RPI, send IP upon being pressed

# Wait till RPi settles
time.sleep(10)

gmail_user = "homeauto112@gmail.com"
gmail_password = "Livhuwani$12"
to  = "mpho112@gmail.com"

mail_server = smtplib.SMTP('smtp.gmail.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.login(gmail_user, gmail_password)
today = datetime.date.today()

arg='ip route list'
p=subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
extipaddr = urllib2.urlopen("http://icanhazip.com").read().strip()

my_ip = 'Local address: {}\nExternal address: {}'.format(ipaddr, extipaddr)
LOGGER.info('Local IP:,{},Ext IP,:{}'.format(ipaddr, extipaddr))

msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
mail_server.sendmail(gmail_user, [to], msg.as_string())
mail_server.quit()
