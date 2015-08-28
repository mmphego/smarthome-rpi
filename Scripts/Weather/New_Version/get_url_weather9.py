#!/usr/bin/python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.1 $"
__description__ = "Weather retrieval"
__date__ = "$Date: 2015/01/30 12:47$"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import urllib2
import json

# get Id from  http://openweathermap.org/find?q=
pretoria = '964137'
cape_town = '3369157'

# Get weather
request = urllib2.Request('http://api.openweathermap.org/data/2.5/weather?id={}&units=metric'.format(cape_town))
# Get todays forecast
request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/forecast/daily?id=964137&units=metric')

try:
    weather_api = urllib2.urlopen(request)
    response = weather_api.read()
    response_dictionary = json.loads(response)

    current = response_dictionary['main']['temp']
    current_low = response_dictionary['main']['temp_min']
    current_high = response_dictionary['main']['temp_max']
    conditions = response_dictionary['weather'][0]['description']

    current = round(current,1)
    current_low = round(current_low,1)
    current_high = round(current_high,1)

    # reads current weather
    wtr = 'Weather conditions for today are ' + str(conditions) + ' with a current temperature of ' + str(current)
except Exception:
    wtr = 'Failed to connect to Open Weather Map.  '

try:
    forecast_api  = urllib2.urlopen(request_2)
    response_2 = forecast_api.read()
    response_2_dictionary = json.loads(response_2)

    todays_low = response_2_dictionary['list'][0]['temp']['night']
    todays_high = response_2_dictionary['list'][0]['temp']['day']

    todays_low = round(todays_low,1)
    todays_high = round(todays_high,1)

    frc = ' a low of ' + str(todays_low) + ' and a high of  ' + str(todays_high) + ' .  '

except Exception:
    frc = 'Failed to connect to Open Weather Map.  '

print wtr, frc
