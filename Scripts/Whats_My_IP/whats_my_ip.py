#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.3$"
__description__ = "Finds IP on startup and email the user if it changed."

import smtplib
import datetime
import urllib2
import time
import subprocess

from logger import LOGGER
from email.mime.text import MIMEText
from pushbullet import Pushbullet
from yamlConfigFile import configFile
# TODO: MM: 2015-10-15: Include button for RPI, send IP upon being pressed

user = configFile()['Email']
password = configFile()['EmailPassword']
to = configFile()['Email2']
api_key = configFile()['PushNotifications']['Pushbullet']
# Wait till RPi settles
time.sleep(10)

subprocess.call(['sudo', 'chown', '-Rh', 'pi:pi', '/home/pi/Logs/'])
subprocess.call(['sudo', 'chmod', '-R', '+w', '/home/pi/Logs'])

def pushNotification(apikey, new_ip_add=None):

    notify_success = False
    try:
        pb = Pushbullet(apikey)
    except:
        return False
    else:
        notify_success = pb.push_note('New RPi IP', new_ip_add)['active']
    return notify_success

def check_ip():
    Prev_IP = None
    with open('/home/pi/Logs/IP_Logger.csv', 'rb') as csv_file:
        # check if prev ip exists
        lines = csv_file.readlines()
        for i in range(-1, -len(lines) - 1, -1):
            if "Local IP" in lines[i]:
                Prev_IP = [x.strip() for x in lines[i].split(',')][-1]
                break
            else:
                continue

    Send_IP = Find_IP(user, password, to)
    Send_IP.find_ip()
    New_IP = Send_IP.ip_addr
    if New_IP != Prev_IP:
        LOGGER.info('Email sent with new ip: {}'.format(New_IP))
        pushNotification(api_key, New_IP)
        Send_IP.send_mail()
    else:
        LOGGER.info("IP Address hasn't changed")


class Find_IP(object):
    def __init__(self, gmail_user, gmail_password, sendto):
        self.gmail_password = gmail_password
        self.gmail_user = gmail_user
        self.sendto = sendto

    def _email_config(self):
        try:
            self.mail_server = smtplib.SMTP('smtp.gmail.com', 587)
            self.mail_server.ehlo()
            self.mail_server.starttls()
            self.mail_server.login(self.gmail_user, self.gmail_password)

        except:
            LOGGER.exception("Failed to connnect.")
            exit()

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
