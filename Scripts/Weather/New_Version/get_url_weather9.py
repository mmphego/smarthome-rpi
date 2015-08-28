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
import decimal

request = urllib2.Request('http://api.openweathermap.org/data/2.5/weather?id=964137&units=metric')
#http://api.openweathermap.org/data/2.5/weather?id=964137&units=metric
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
#    print current
#    f=open('/home/pi/test.txt','wb')    
#    f.write(str(current))
#    f.close()

#    print current_low
#    print current_high
#    print conditions

    # reads current weather
    wtr = 'Weather conditions for today are ' + str(conditions) + ' with a current temperature of ' + str(current)
except urllib2.HTTPError, e:
    wtr = 'Failed to connect to Open Weather Map.  '
except urllib2.URLError, e:
    wtr = 'Failed to connect to Open Weather Map.  '
except Exception:
    wtr = 'Failed to connect to Open Weather Map.  '

#print wtr

request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/forecast/daily?id=964137&units=metric')

try: 
    forecast_api  = urllib2.urlopen(request_2)
    response_2 = forecast_api.read()
    response_2_dictionary = json.loads(response_2)
#    print response_2_dictionary
    todays_low = response_2_dictionary['list'][0]['temp']['night']
    todays_high = response_2_dictionary['list'][0]['temp']['day']

    todays_low = round(todays_low,1)
    todays_high = round(todays_high,1)
    
    frc = '  with a low of ' + str(todays_low) + ' and a high of  ' + str(todays_high) + ' .  '

except urllib2.HTTPError, e:
    frc = 'Failed to connect to Open Weather Map.  '
except urllib2.URLError, e:
    frc = 'Failed to connect to Open Weather Map.  '
except Exception:
    frc = 'Failed to connect to Open Weather Map.  '

print frc


