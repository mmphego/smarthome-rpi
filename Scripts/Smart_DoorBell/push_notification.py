#!/usr/bin/env python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.0 $"
__description__ = "Real-time notifications on your Android mobile"
__date__ = "$Date: 2015/09/10 11:55 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

try:
    from pushover import init, Client, time
except ImportError:
    import pip
    pip.main(['install', 'python-pushover'])

# https://pushover.net
def send_notification():
    init('aBvnvKsL6YSDxDdkDkQehkoGH4m6oo')
    client = Client('uUJ7mE5whHv8273LFF9c38niv1w8gj').send_message(
        "Hello!, Someone is at the door at {}".format(time.ctime()),
            title="The is someone at the door.")
