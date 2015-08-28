#!/usr/bin/python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.2 $"
__description__ = "Weather retrieval"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import urllib2
import json

try:
    # get current city using geo ip location
    geoip = urllib2.Request('http://www.telize.com/geoip')
    geoip_read = urllib2.urlopen(geoip).read()
    geoip_loc = str(json.loads(geoip_read)['city'])
    # Get todays weather
    request = urllib2.Request('http://api.openweathermap.org/data/2.5/'
        'weather?q={}&units=metric'.format(geoip_loc))
    # Get forecast
    request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/'
        'forecast/daily?q={}&units=metric'.format(geoip_loc))

except Exception:
    request = urllib2.Request('http://api.openweathermap.org/data/2.5/'
        'weather?q=pretoria&units=metric')
    request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/'
        'forecast/daily?q=pretoria&units=metric')

try:
    weather_api = urllib2.urlopen(request)
    response = weather_api.read()
    response_dictionary = json.loads(response)

    forecast_api  = urllib2.urlopen(request_2)
    response_2 = forecast_api.read()
    response_2_dictionary = json.loads(response_2)

except Exception:
    wtr = 'Failed to connect to Open Weather Map.  '

current = response_dictionary['main']['temp']
current_low = response_dictionary['main']['temp_min']
current_high = response_dictionary['main']['temp_max']
conditions = response_dictionary['weather'][0]['description']

current = str(round(current, 1)).replace('.', ' point ')
current_low = str(round(current_low, 1)).replace('.', ' point ')
current_high = str(round(current_high, 1)).replace('.', ' point ')

todays_low = response_2_dictionary['list'][0]['temp']['night']
todays_high = response_2_dictionary['list'][0]['temp']['day']

todays_low = str(round(todays_low, 1)).replace('.', ' point ')
todays_high = str(round(todays_high, 1)).replace('.', ' point ')

wtr = ('Weather conditions for today, ' + conditions +
    ' with a current temperature of ' + current)
frc = (', a low of ' + todays_low + ' and a high of  '
    + todays_high + ' .  ')
