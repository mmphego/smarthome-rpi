#!/usr/bin/python
__author__ = "Mpho Mphego"
__version__ = "$Revision: 1.2 $"
__description__ = "Weather retrieval"
__copyright__ = "Copyright (c) 2015 Mpho Mphego"
__url__ = "mpho112.wordpress.com"
__license__ = "Python"

import urllib2
import json
from yamlConfigFile import configFile
#from logger import LOGGER

api_key = configFile()['APIs']['openWeatherAPI']
# get current city using geo ip location
geoip = urllib2.Request('http://ip-api.com/json')
geoip_read = json.loads(urllib2.urlopen(geoip).read())
if geoip_read['status'] == 'success':
    geoip_city = str(geoip_read['city'])
    geoip_country = str(geoip_read['countryCode'])
    geoip_zip = str(geoip_read['zip'])
    #if geoip_country == 'ZA': geoip_country = 'SA'
    geoip_coord = (geoip_read['lon'],
        geoip_read['lat'])
else:
    geoip_config = configFile()['geography']
    geoip_city = geoip_config['city']
    geoip_country = geoip_config['country']
    geoip_zip = geoip_config['code']
    geoip_coord = geoip_config['coord'].split(',')

# Get todays weather
request = ('http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'.format(
            geoip_city.replace(' ','').lower(), geoip_country, api_key))

#request = urllib2.Request('http://api.openweathermap.org/data/2.5/'
#    'weather?q={},{}&units=metric'.format(geoip_city, geoip_country))

# Get forecast
request_2 = ('http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&cnt=1&units=metric&appid={}'
    .format(geoip_coord[1], geoip_coord[0], api_key))

#except Exception:
    #request = urllib2.Request('http://api.openweathermap.org/data/2.5/'
        #'weather?q=pretoria&units=metric')
    #request_2 = urllib2.Request('http://api.openweathermap.org/data/2.5/'
        #'forecast?lat=18.4&lon=-33.9833&cnt=1&units=metric')


weather_api = urllib2.urlopen(request)
response = weather_api.read()
response_dictionary = json.loads(response)
weather_api.close()
forecast_api  = urllib2.urlopen(request_2)
response_2 = forecast_api.read()
response_2_dictionary = json.loads(response_2)
forecast_api.close()

try:
    current = response_dictionary['main']['temp']/10.
    current_low = response_dictionary['main']['temp_min']
    if current_low > 50:
        current_low = current_low/10.
    current_high = response_dictionary['main']['temp_max']
    if current_high > 50:
        current_high = current_high/10.
    conditions = response_dictionary['weather'][0]['description']
except KeyError:
    #LOGGER.error('Unable to read links')
    raise RuntimeError('Unable to read links')

current = str(round(current, 1)).replace('.', ' point ')
current_low = str(round(current_low, 1)).replace('.', ' point ')
current_high = str(round(current_high, 1)).replace('.', ' point ')
todays_low = response_2_dictionary['list'][0]['main']['temp_min']
todays_high = response_2_dictionary['list'][0]['main']['temp_max']

todays_low_str = str(round(todays_low, 1)).replace('.', ' point ')
todays_high_str = str(round(todays_high, 1)).replace('.', ' point ')

#LOGGER.info('Max:, {}, Min:, {}'.format(todays_high, todays_low))
wtr = ('Weather conditions for today, ' + conditions +
    ' with a current temperature of ' + current)
frc = (', a low of ' + todays_low_str + ' and a high of  '
    + todays_high_str + ' .  ')

print wtr + frc
