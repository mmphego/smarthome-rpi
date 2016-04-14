try:
    import Adafruit_DHT as dht
except ImportError:
    import pip
    pip.main(['install', 'Adafruit_DHT'])

import time
import urllib2
import gc
import os
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
while True:
    humidity, temperature = getSensorData()
    ostemp = os.popen('vcgencmd measure_temp').readline()
    cpu_temp = (ostemp.replace("temp=", "").replace("'C\n", ""))
    LOGGER.info('Humidity: {}%, Temp: {}, CPU_Temp: {}'.format(humidity, temperature, cpu_temp))
    try:
        send_data = urllib2.urlopen(API_URL + '&field1={}&field2={}&field3={}'.format(humidity, temperature, cpu_temp))
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
