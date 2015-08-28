#!/usr/bin/env python

import os
fh=open("/home/pi/Scripts/Weather/.weather_after.txt")
for line in fh.readlines():
    if 'rain' in line.split():
        line =  line.rstrip().split()
        temp = line[2:3]
        temp = int(max(temp))
        if temp < 20 :
#            print "It might rain "
            os.system("mpg123 /home/pi/Scripts/ClosetDoorWarning/rain_warning.mp3")
        else:
            print "It might rain, but change later in the day"
            os.system("mpg123 /home/pi/Scripts/ClosetDoorWarning/light_rain_warning.mp3")
    else:
        if temp > 20 :
            print "Weather is perfect"
            os.system("mpg123 /home/pi/Scripts/ClosetDoorWarning/no_rain_warning.mp3")
