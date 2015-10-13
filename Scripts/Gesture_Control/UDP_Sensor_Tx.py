try:
    # Android API Object SL4A Specific
    import android
except:
    import androidhelper as android
import time
import socket

droid = android.Android()

try:
    droid.ttsSpeak("Please enter server's IP address")
    time.sleep(.5)
    #hostname = "192.168.1.173"
    hostname = str(droid.dialogGetInput(title='IP Address').result)
    port = 5005
    message = "Connecting to hostname:{}, port:{}".format(hostname, port)
    droid.makeToast(hostname)
except Exception as e:
    droid.ttsSpeak('Failed to get IP address.')

data = str()
ts = 100  # max sampling time 100ms
timeout = 0.5
Accelerometer = 2
try:
    # Creating a UDP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Connecting to Host (Usually not required since it is UDP)
    s.connect((hostname, port))
    droid.makeToast("Connected to server!")
except Exception as e:
    droid.ttsSpeak('Not connected to host due to {}!'.format(e))
    droid.makeToast('Failed: {}'.format(e))

# start sensing Accelerometer at 100ms
droid.startSensingTimed(Accelerometer, ts)
exit = False
while not exit:
    sensor_data = str(droid.sensorsReadAccelerometer().result)
    try:
        time.sleep(timeout)
        s.sendto(sensor_data, (hostname, port))
        s.settimeout(timeout)
    except Exception as e:
        droid.makeToast(' Could not connect to host, Error: {}'.format(e))
        droid.ttsSpeak('Failed to send data to host!')
        droid.stopSensing()
        exit = True

