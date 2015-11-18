import plotly
import plotly.plotly as py
import plotly.tools as tls

import time
import datetime
import random

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
            'maxpoints': 20
        }
    }], filename=' Streaming Example Values')

print "View your streaming graph here: ", url

# temperature sensor middle pin connected channel 0 of mcp3008

stream = py.Stream(stream_id)
stream.open()

#the main sensor reading and plotting loop
while True:
    # write the data to plotly
    stream.write({'x': datetime.datetime.now(), 'y': random.randrange(1, 10)})

    # delay between stream posts
    time.sleep(1)
