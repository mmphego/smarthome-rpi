import csv
import time
import Adafruit_DHT as dht

data = list(dht.read_retry(dht.DHT11, 26))
path = "/home/pi/Logs/Temp_Humid.csv"

#----------------------------------------------------------------------
def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(data)

#----------------------------------------------------------------------
if __name__ == "__main__":

    while True:
        csv_writer(data, path)
        time.sleep(10)
