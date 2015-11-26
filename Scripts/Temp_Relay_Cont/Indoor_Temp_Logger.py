try:

    import plotly
except ImportError:
    import pip
    pip.main(['install', 'plotly'])

try:
    import Adafruit_DHT as dht
except ImportError:
    import pip
    pip.main(['install', 'Adafruit_DHT'])

import csv
import plotly.plotly as py
import plotly.tools as tls
import time
import datetime
import random


pin = 26
data = list(dht.read_retry(dht.DHT11, pin))
path = "../../Logs/Temp_Humid.csv"

#----------------------------------------------------------------------
def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(data)

plotly.tools.set_credentials_file(
    username='MphoMphego',
    api_key='o7duum0tjv',
    stream_ids=['05wy3vh4ir', 'odash4fbv3','0o2e9ojx6h'])

stream_id = tls.get_credentials_file()['stream_ids'][0]

url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': stream_id,
            'maxpoints': 200
        }
    }], filename='Indoor Temp Ploter')

print "View your streaming graph here: ", url

# temperature sensor middle pin connected channel 0 of mcp3008

stream = py.Stream(stream_id)
stream.open()



#----------------------------------------------------------------------
if __name__ == "__main__":

    #the main sensor reading and plotting loop
    while True:
        # write the data to plotly
        stream.write({'x': datetime.datetime.now(), 'y': random.randrange(1, 10)})

        csv_writer(data, path)
        # delay between stream posts
        time.sleep(10)
