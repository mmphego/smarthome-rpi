try:
    # Android API Object SL4A Specific
    import android
except:

    import androidhelper as android
import time
import socket

droid = android.Android()
hostname = "192.168.1.173"
try:
    if hostname > len(0):
        pass
except Exception as e:
    droid.ttsSpeak(' data to host!')
    hostname = str(droid.dialogGetInput().result)

port = 5005
data = ""
ts = 100 # max sampling time 100ms
tc = 1000 # cut of sampling time 1000ms
t = 0
try:

    # Creating a UDP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    # Connecting to Host (Usually not required since it is UDP)
    s.connect((hostname,port));
    print "Connected!";
except Exception as e:
    droid.ttsSpeak('Not connected to host!')
    print 'Failed: {}'.format(e)


droid.startSensingTimed(2, ts) # start sensing accelerometer

exit = False
while not exit:
    sensor_data = str(droid.sensorsReadAccelerometer().result)
    try:
        s.sendto(sensor_data,(hostname,port));
        time.sleep(.5)
    except Exception as e:
        print ' Could not connect to host, Error: {}'.format(e)
        droid.ttsSpeak('Failed to send data to host!')
        exit = True
        break
