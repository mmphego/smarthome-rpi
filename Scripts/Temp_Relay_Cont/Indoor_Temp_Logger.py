import time
import Adafruit_DHT as dht

while True:
    with open('/home/pi/Logs/Temp_Humid.log','w') as fh:
        import IPython
        varTemp, varHum = dht.read_retry(dht.DHT11, 26)
        fh.write(list(dht.read_retry(dht.DHT11, 26)))
    time.sleep(10)
