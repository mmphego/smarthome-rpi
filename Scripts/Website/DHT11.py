import time
import Adafruit_DHT as dht

varTemp, varHum = dht.read_retry(dht.DHT11, 26)
print varTemp, varHum
