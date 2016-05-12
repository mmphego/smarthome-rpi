import androidhelper as android
import time
import math

droid = android.Android()
ts = 100 # max sampling time 100ms
tc = 1000 # cut of sampling time 1000ms
t = 0
droid.startSensingTimed(2, ts) # start sensing accelerometer
while True:
    print droid.sensorsReadAccelerometer().result
    x_data, y_data, z_data = droid.sensorsReadAccelerometer().result

    time.sleep(ts/1000.0)
    t += tc
droid.stopSensing()
