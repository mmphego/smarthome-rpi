#!/usr/bin/python2
__author__ = "Mpho Mphego"
__description__ = "Home Automation Webserver and Control Center"
__version__ = "$Revision: 2.0 $"
__date__ = "$Date: 2015/01/22 22:54 $"
__url__ = "mpho112.wordpress.com"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__license__ = "Python/HTML"

import sys
import os
from wsgiref.simple_server import make_server
from urlparse import parse_qsl
from html_site import html
from yamlConfigFile import configFile

sys.path.insert(1, '/home/pi/Scripts/Relay_Control/')
from relay_control import *
try:
    locals().update(relays_conf)
except:
    pass

rst_counter = 0
def gesture_switch_on(pin):
        global rst_counter
        rst_counter += 1
        relay_on(pin)
def gesture_switch_off(pin):
        global rst_counter
        rst_counter = 0
        relay_off(pin)


def application(environ, start_response):
    """Returns a dictionary containing lists as values."""
    d = parse_qsl(environ['QUERY_STRING'])

    try:
        if (d[0][0]=="led1"):
            gesture_switch_on(Relay1)
            if rst_counter > 1:
                gesture_switch_off(Relay1)
        if (d[0][0]=="led2"):
            gesture_switch_on(Relay2)
            if rst_counter > 1:
                gesture_switch_off(Relay2)

        if (d[0][0]=="led3"):
            gesture_switch_on(Relay3)
            if rst_counter > 1:
                gesture_switch_off(Relay3)

        if (d[0][0]=="led4"):
            gesture_switch_on(Relay4)
            if rst_counter > 1:
                gesture_switch_off(Relay4)

        if (d[0][0]=="led5"):
            gesture_switch_on(Relay1)
            relay_on(Relay2)
            relay_on(Relay3)
            relay_on(Relay4)
            if rst_counter > 1:
                gesture_switch_off(Relay1)
                gesture_switch_off(Relay2)
                gesture_switch_off(Relay3)
                gesture_switch_off(Relay4)
                relay_off(Relay1)
                relay_off(Relay2)
                relay_off(Relay3)
                relay_off(Relay4)

    except:
        pass
    response_body = html()
    status = '200 OK'

    # Now content type is text/html
    response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

httpd = make_server('0.0.0.0', 8000, application)
# Now it is serve_forever() in instead of handle_request().
# In Linux a Ctrl-C will do it.
#reloader.install()
httpd.serve_forever()
#httpd.handle_request()
