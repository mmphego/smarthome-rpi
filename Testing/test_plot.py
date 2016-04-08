import plotly.plotly as py
import plotly.tools as tls

import time
import datetime
import random

stream_id = tls.get_credentials_file()['stream_ids'][0]

#with open('./config.json') as config_file:
#    plotly_user_config = json.load(config_file)

#py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': stream_id,
            'maxpoints': 200
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
    time.sleep(0.25)

