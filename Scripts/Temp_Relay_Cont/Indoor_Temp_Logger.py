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
from logger import LOGGER

wait_time = 30
pin = 26

baseurl = 'https://api.thingspeak.com/update?api_key='
apikey = 'H4KN07GGESD8XZEH'

def getSensorData():
    try:
        humid, temp = dht.read_retry(dht.DHT11, pin)
    except:
        return None
        raise RuntimeError('unable to read sensor')
    return (str(humid), str(temp))

#----------------------------------------------------------------------

API_URL = baseurl + apikey
count = 0

sensor_name_1 = 'raspberry_pi_cputemp'
sensor_name_2 = 'DHT11_Temp'
sensor_name_3 = 'DHT11_Humidity'
while True:
    humidity, temperature = getSensorData()
    ostemp = os.popen('vcgencmd measure_temp').readline()
    cpu_temp = (ostemp.replace("temp=", "").replace("'C\n", ""))
    LOGGER.info('Humidity: {}%, Temp: {}, CPU_Temp: {}'.format(humidity, temperature, cpu_temp))
    try:
        send_data = urllib2.urlopen(API_URL +
            '&field1={}&field2={}&field3={}&field4={}&field5={}'.format(
            humidity, temperature, cpu_temp, psutil.net_io_counters().bytes_sent,
            psutil.net_io_counters().bytes_recv))
        dweepy.dweet_for(sensor_name_1, {'CPU_Temp': cpu_temp})
        dweepy.dweet_for(sensor_name_2, {'Ambi_Temp': temperature})
        dweepy.dweet_for(sensor_name_3, {'Ambi_Hum': humidity})

    except:
        count += 1
        send_data.close()
        if count > 5:
            raise RuntimeError('Failed to reach url')
            break
            count = 0
    time.sleep(wait_time)
    send_data.close()
gc.collect()
