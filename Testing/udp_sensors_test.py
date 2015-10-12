import androidhelper as android
import time
import socket

droid = android.Android()
ts = 100 # max sampling time 100ms
tc = 1000 # cut of sampling time 1000ms
t = 0
droid.startSensingTimed(2, ts) # start sensing accelerometer

hostname = "192.168.1.173"
port = 5005
data = ""
try:
    # Creating a UDP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Connecting to Host (Usually not required since it is UDP)
    s.connect((hostname,port))
    print "Connected!"
except Exception as e:
    print 'Failed: {}'.format(e)

while True:
    print STR(droid.sensorsReadAccelerometer().result
    x_data, y_data, z_data = droid.sensorsReadAccelerometer().result

    time.sleep(.5)
    #time.sleep(ts/1000.0)
    #t += tc
droid.stopSensing()
