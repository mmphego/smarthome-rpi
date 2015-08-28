#!/usr/bin/python
__author__ = "Mpho Mphego"
__description__ = "Graphite System Crawler: CPU Usage"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2014/07/12 02:54 $"
__url__ = "mpho112.wordpress.com"
__copyright__ = "Copyright (c) 2014 Mpho Mphego"
__license__ = "Python"

import sys
import time
import os
import platform 
import subprocess
from socket import socket

#Diagnostics
#***********************************************************************************************
def systemDiagnostics():
# This section of the script is for retrieving general system diagnostics
# The load average section is taken and apadapted from the example-cliet.py in the graphite directory
    print "Retrieving system information"
    lines = []
    nowTime = int(time.time())
    metric = "carbon.rpi.system."
  # For more details, "man proc" and "man uptime"  
    if platform.system() == "Linux":
        output = open('/proc/loadavg').read().strip().split()[:3]
    else:   
        command = "uptime"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        os.waitpid(process.pid, 0)
        outputCMD = process.stdout.read().replace(',', ' ').strip().split()
        length = len(output)
        nowTime = int( time.time() )
        output = outputCMD[length - 3:length]
    lines.append("%sloadAvg_1min %s %s" %(metric,output[0],nowTime))
    lines.append("%sloadAvg_5min %s %s" %(metric,output[1],nowTime))
    lines.append("%sloadAvg_15min %s %s" %(metric,output[2],nowTime))
    print lines
    message = '\n'.join(lines) + '\n'
    print "System information retrieved"
    
    return message
                 
#***********************************************************************************************



# MAIN
#***********************************************************************************************
CARBON_SERVER = '172.18.20.41'
CARBON_PORT = 2003
sock = socket()
#sock.settimeout( 5.0)

try:
  sock.connect( (CARBON_SERVER,CARBON_PORT) )
except:
  print "Couldn't connect to %(server)s on port %(port)d, is carbon-agent.py running?" % { 'server':CARBON_SERVER, 'port':CARBON_PORT }
  #sys.exit(1)

# Infinite loop to keep things going 
while True:
    message = systemDiagnostics()
    try:
        print "Sending message..."
        sock.sendall(message)
        print "Message sent."
        print '-' * 80        
    except:
#	sock.settimeout( 5.0)
        print "Could not connect to Graphite server, trying to reconnect...."
        time.sleep(5)
        try:   
            del sock
            sock = socket.socket()
            sock.connect((graphite_server, graphite_port))
        except:
            print "Reconnection attempt failed...Retrying..." 
    time.sleep(10)
sock.close

#***********************************************************************************************

