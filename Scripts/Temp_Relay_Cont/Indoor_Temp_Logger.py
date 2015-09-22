import time
import Adafruit_DHT as dht

while True:
    with open('/home/pi/Logs/Temp_Humid.log','w') as fh:
        fh.write(str(dht.read_retry(dht.DHT11, 26)))
    time.sleep(10)
