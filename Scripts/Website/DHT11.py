import time
import Adafruit_DHT as dht

with open('Temp_Humid.log') as fh:
    fh.write(dht.read_retry(dht.DHT11, 26))
#varTemp, varHum = dht.read_retry(dht.DHT11, 26)
#print varTemp, varHum
