#!/usr/bin/env python2.7
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.2 $"
__description__ = "Closet Door sensor for warning against Rain"
__date__ = "$Date: 2015/01/14 01:59 $"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import os
import csv
from collections import deque
from logger import LOGGER

csv_file = '../../Scripts/Weather/New_Version/Weather_Logger.csv'

def get_last_row(csv_filename):
    with open(csv_filename, 'rb') as f:
        try:
            return deque(csv.reader(f), 1)[0]
        except Exception:
            LOGGER.error('Could not read CSV either file doesnt exist or error'
                ' reading it')

def notification():
    temp_min = float(get_last_row(csv_file)[-1])
    if temp_min < 10. :
        os.system("mpg123 rain_warning.mp3")
    elif temp_min >= 10. and temp_min <= 20.:
        os.system("mpg123 light_rain_warning.mp3")
    else:
        os.system("mpg123 no_rain_warning.mp3")
