#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.3$"
__description__ = "Finds IP on startup and email the user if it changed."

import subprocess
import smtplib
import datetime
import urllib2
import csv
import time
from logger import LOGGER
from email.mime.text import MIMEText
from collections import deque


# TODO: MM: 2015-10-15: Include button for RPI, send IP upon being pressed
user = "homeauto112@gmail.com"
password = "Livhuwani$12"
to = "mpho112@gmail.com"
# Wait till RPi settles
time.sleep(10)


def check_ip():
    with open('../../Logs/IP_Logger.csv', 'rb') as csv_file:
        Prev_IP = deque(csv.reader(csv_file), 1)[0][-1]

    Send_IP = Find_IP(user, password, to)
    Send_IP.find_ip()
    New_IP = Send_IP.ip_addr
    if Prev_IP != New_IP:
        LOGGER.info('Email send with new ip: {}'.format(New_IP))
        Send_IP.send_mail()
    else:
        LOGGER.info("IP Address hasn't changed")


class Find_IP(object):
    def __init__(self, gmail_user, gmail_password, sendto):
        self.gmail_password = gmail_password
        self.gmail_user = gmail_user
        self.sendto = sendto

    def _email_config(self):
        self.mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        self.mail_server.helo()
        self.mail_server.starttls()
        self.mail_server.login(self.gmail_user, self.gmail_password)

    def find_ip(self):
        arg = 'ip route list'
        p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
        data = p.communicate()
        split_data = data[0].split()
        self.ip_addr = split_data[split_data.index('src') + 1]
        self.ext_ipaddr = urllib2.urlopen("http://icanhazip.com").read().strip()
        LOGGER.info('Local IP:,{}'.format(self.ip_addr))

    def force_send(self):
        """
        Configure emergency button
        """
        pass

    def send_mail(self):
        self._email_config()
        self.find_ip()
        ip_address = 'Local address: {}\nExternal address: {}'.format(self.ip_addr, self.ext_ipaddr)
        today = datetime.date.today()
        msg = MIMEText(ip_address)
        msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
        msg['From'] = self.gmail_user
        msg['To'] = to
        self.mail_server.sendmail(self.gmail_user, [to], msg.as_string())
        self.mail_server.quit()


# Run check IP , if changed send email.
check_ip()
