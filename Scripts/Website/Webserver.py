#!/usr/bin/python2
__author__ = "Mpho Mphego"
__description__ = "Home Automation Webserver and Control Center"
__version__ = "$Revision: 2.0 $"
__date__ = "$Date: 2015/01/22 22:54 $"
__url__ = "mpho112.wordpress.com"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__license__ = "Python/HTML"

from wsgiref.simple_server import make_server
from urlparse import parse_qsl
import os
import time
from html_site import html


def application(environ, start_response):
    """Returns a dictionary containing lists as values."""
    d = parse_qsl(environ['QUERY_STRING'])

    try:
        if (d[0][0]=="led1"): os.system("home_auto 1 > /dev/null 2>&1")
        if (d[0][0]=="led2"): os.system("home_auto 2 > /dev/null 2>&1")
        if (d[0][0]=="led3"): os.system("home_auto 3 > /dev/null 2>&1")
        if (d[0][0]=="led4"): os.system("home_auto 4 > /dev/null 2>&1")
        if (d[0][0]=="led5"): os.system("home_auto 5 > /dev/null 2>&1")
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
