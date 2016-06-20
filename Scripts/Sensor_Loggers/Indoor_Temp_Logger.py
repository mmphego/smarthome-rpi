try:
    import Adafruit_DHT as dht
except ImportError:
    import pip
    pip.main(['install', 'Adafruit_DHT'])

import time
import urllib2
import gc
import os
import dweepy
import psutil
import sys

from logger import LOGGER
from yamlConfigFile import configFile
from Notifier import Notification

sys.path.insert(1, '/home/pi/Scripts/Smoke_Detection/')
sys.path.insert(1, '/home/pi/Scripts/Light_sensor/')
import Smoke_Detection
from ldr_sensor import RCtime
from ldr_sensor import cleanup

#cleanup()
wait_time = 30
pin = 26
ldr_pin = 16

baseurl = 'https://api.thingspeak.com/update?api_key='

username = configFile()['Email']
password = configFile()['EmailPassword']
send_to = configFile()['Email2']
Notify_api_key = configFile()['PushNotifications']['Pushbullet']

apikey = configFile()['APIs']['thingspeak']

def getSensorData():
    try:
        humid, temp = dht.read_retry(dht.DHT11, pin)
    except:
        return (0, 0)
    return (str(humid), str(temp))

def getGasSensorData():
    try:
        if Smoke_Detection.get_gas_sensor() is not None:
            smoke_val = Smoke_Detection.get_gas_sensor()
            print smoke_val
        else:
            smoke_val = 0
    except:
        smoke_val = 0
    return str(smoke_val)

def getLightLevels(LDR_pin):
    try:
        if RCtime(LDR_pin) is not None:
             light_val = RCtime(LDR_pin)
        else:
            raise Exception
    except:
         light_val = 0
    return light_val

def getCPUTemp():
    try:
        ostemp = os.popen('vcgencmd measure_temp').readline()
        cpu_temp = (ostemp.replace("temp=", "").replace("'C\n", ""))
    except:
        cpu_temp = 0
    return cpu_temp

#----------------------------------------------------------------------

API_URL = baseurl + apikey
count = 0
rst_counter = 0

sensor_name_1 = 'raspberry_pi_cputemp'
sensor_name_2 = 'DHT11_Temp'
sensor_name_3 = 'DHT11_Humidity'

NotifyMe = Notification(username, password, send_to, Notify_api_key)

def notification(alert, message):
    global rst_counter
    rst_counter += 1
    NotifyMe.send_mail(alert, message)
    NotifyMe.send_pushbullet(alert, message)

def notification_check():
    global rst_counter
    rst_counter = 0

try:
    while True:
        smoke = getGasSensorData()
        light = getLightLevels(ldr_pin)
        humidity, temperature = getSensorData()
        cpu_temp = getCPUTemp()

        LOGGER.info('Humidity: {}%, Temp: {}, CPU_Temp: {}, Smoke_Level: {}, Light_Levels: {}'.format(
            humidity, temperature, cpu_temp, smoke, light))

        print ('Humidity: {}%, Temp: {}, CPU_Temp: {}, Smoke_Level: {}, Light_Levels: {}'.format(
            humidity, temperature, cpu_temp, smoke, light))

        #if float(temperature) > 35.:
            #alert = 'Temperature Nofication'
            #message = 'Temperature is at {}degrees'.format(temperature)
            #notification(alert, message)
            #if rst_counter > 1:
                #notification_check()

        #if float(humidity) > 50.:
            #alert = 'Humidity Nofication'
            #message = 'Humidity is at {}%'.format(humidity)
            #notification(alert, message)
            #if rst_counter > 1:
                #notification_check()

        #if float(smoke) > 450.:
            #alert = 'Smoke Nofication'
            #message = 'Smoke is at {}'.format(smoke)
            #notification(alert, message)
            #if rst_counter > 1:
                #notification_check()

        try:
            send_data = urllib2.urlopen(API_URL +
                '&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}&field7={}'.format(
                humidity, temperature, cpu_temp, 0,0, smoke, light))
            #dweepy.dweet_for(sensor_name_1, {'CPU_Temp': cpu_temp})
            #dweepy.dweet_for(sensor_name_2, {'Ambi_Temp': temperature})
            #dweepy.dweet_for(sensor_name_3, {'Ambi_Hum': humidity})

        except:
            count += 1
            send_data.close()
            if count > 5:
                count = 0
        time.sleep(wait_time)
        send_data.close()
        gc.collect()
except:
    cleanup()
