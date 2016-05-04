#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.0 $"
__description__ = "Real-time notifications on your Android mobile"
__date__ = "$Date: 2015/09/10 11:55 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import os
from logger import LOGGER
try:
    import pushover, pynma, instapush
except ImportError:
    import pip
    pip.main(['install', 'python-pushover'])
    pip.main(['install', 'pynma'])
    pip.main(['install', 'instapush'])
    pip.main(['install', 'pushbullet.py'])
finally:
    from pushover import init, Client, time
    from pynma import PyNMA
    from instapush import Instapush, App
    from pushbullet import Pushbullet

from yamlConfigFile import configFile

Api_Keys = configFile()['PushNotifications']
message = "Hello!, Someone is at the door at {}".format(time.ctime())
alert = "There is someone at the door."
image_path = "/home/pi/Scripts/Smart_DoorBell/image.jpg"

# https://pushbullet.net
def send_pushbullet():
    LOGGER.info('Sending Pushbullet notification')
    api_key = configFile()['PushNotifications']['Pushbullet']
    push_success = False
    try:
       pb = Pushbullet(api_key)
    except :
        LOGGER.error ('Unable to connect to pushover server')
        raise RuntimeError ('Unable to connect to pushover server')
    else:
        if os.path_exists(image_path):
            with open(image_path, "rb") as pic:
                file_data = pb.upload_file(pic, "picture.jpg")
            push_success = pb.push_file(**file_data)['active']
        else:
            push_success = pb.push_note(alert, message)['active']

    if push_success:
        return True
    else:
        return False

def send_nma():
    LOGGER.info('Sending nma notification')

    nma_api_key = Api_Keys['notify_my_android_api_key']
    p = PyNMA(apikey = nma_api_key)
    reply = p.push(application='alert', event=alert, description=message)
    if str(reply[nma_api_key]['type']) == 'success':
        return True
    else:
        return False

def send_instapush():
    LOGGER.info('Sending instapush notification')

    instapush_api_key = Api_Keys['Instapush_api_key']
    instapush_secret_key = Api_Keys['Instapush_sec_key']
    insta_notify = App(appid=instapush_api_key , secret=instapush_secret_key)
    notify = insta_notify.notify(event_name='alert', trackers={'message':message})
    if notify['error']:
        return False
    else:
        return True

def send_notifications():
    if not send_pushbullet():
        if not send_nma():
            if not send_instapush():
                return False
