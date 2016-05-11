from pubnub import Pubnub

pubnub = Pubnub(publish_key = 'pub-c-5d7fb373-e51d-4ec4-a560-a3833c35d2cd', 
		subscribe_key = 'sub-c-10d4ef38-061e-11e6-8c3e-0619f8945a4f')

def callback(message, channel):
    print(message)
  
  
def error(message):
    print("ERROR : " + str(message))
  
  
def connect(message):
    print("CONNECTED")
    print pubnub.publish(channel='my_channel', message='Hello from the PubNub Python SDK')
  
  
  
def reconnect(message):
    print("RECONNECTED")
  
  
def disconnect(message):
    print("DISCONNECTED")
  
  
pubnub.subscribe(channels='my_channel', callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)
