#!/usr/bin/env python

# Created by Mpho Mphego SANSA Marion Island Engineer 2014-2015
# The purpose of this script is to 

import datetime
import re
import os

data = []
fh=open(".weather_before.txt")
for line in fh.readlines():
    line = line.rsplit()
    line = [ rec.replace("C", "Degrees Celcius") for rec in line ]
    line = [ rec.replace("KPH", "KM per hour") for rec in line ]
    line = [ rec.replace(":", " is") for rec in line ]
    line = " ".join(line) + "."
    data.append(line)
data = " ".join(data)   
#print data  
fh=open(".weather_after.txt","w")
fh.write(data)#print line + "."
fh.close()
    

