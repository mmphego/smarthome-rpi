#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.0 $"
__description__ = "Real-time notifications on your Android mobile"
__date__ = "$Date: 2015/09/10 11:55 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

#from logger import LOGGER
try:
    import pushover, pynma, instapush
except ImportError:
    import pip
    pip.main(['install', 'python-pushover'])
    pip.main(['install', 'pynma'])
    pip.main(['install', 'instapush'])
finally:
    from pushover import init, Client, time
    from pynma import PyNMA
    from instapush import Instapush, App

message = "Hello!, Someone is at the door at {}".format(time.ctime())
alert = "There is someone at the door."

# https://pushover.net
def send_pushover():
    LOGGER.info('Sending Pushover notification')
    pover_api_key = 'aBvnvKsL6YSDxDdkDkQehkoGH4m6oo'
    pover_cl_key = 'uUJ7mE5whHv8273LFF9c38niv1w8gj'
    try:
        init(pover_api_key)
        client = Client(pover_cl_key).send_message(message,
            title = alert)
    except :
        LOGGER.error ('Unable to connect to pushover server')
        raise RuntimeError ('Unable to connect to pushover server')
    if client.answer['status'] == True:
        return True
    else:
        return False

def send_nma():
    LOGGER.info('Sending nma notification')
    nma_api_key = '297e7eed874775b89d8820bbfcefa3caa81b1a71e46e7eae'
    p = PyNMA(apikey = nma_api_key)
    reply = p.push(application='alert', event=alert, description=message)
    if str(reply[nma_api_key]['type']) == 'success':
        return True
    else:
        return False

def send_instapush():
    LOGGER.info('Sending instapush notification')
    instapush_api_key = '570ca43c5659e387177fbb6a'
    instapush_secret_key = 'c31ad2606ce78cf6b52284cb24e72722'
    insta_notify = App(appid=instapush_api_key , secret=instapush_secret_key)
    notify = insta_notify.notify(event_name='alert', trackers={'message':message})
    if notify['error']:
        return False
    else:
        return True

def send_notifications():
    if not send_pushover():
        if not send_nma():
            if not send_instapush():
                return False
