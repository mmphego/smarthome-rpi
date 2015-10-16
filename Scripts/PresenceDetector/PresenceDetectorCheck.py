#!/usr/bin/python2
# Purpose of this script is to ping a certain static IP(android mobile) is destination is
# reachable set a  gpio pin and activate flite(voice response) else if it not detected
# gpio will remain off
# Created by Mpho Mphego (mpho112@gmail.com)
# http://pastebin.com/nLkaZ308

import time
import subprocess

mac_address = 'bc:6e:64:df:d7:d9'

subprocess.call('sudo', 'arp-scan', '--interface', 'wlan0', '-l', '|', 'grep', '{}', '|', 'cut', '-f', '1')

#os.system("gpio mode 7 out")
while True: # Setup a while loop to wait for a button press
    if os.system("ping -c 1 172.18.20.209 > /dev/null 2>&1") == 0:# Send command to os
        print "host is detected"
#        os.system("gpio write 4 0")
#        break
    else:
        print "host unreachable"
        os.system('sudo service cellDetect start')
    break
time.sleep(60) # Allow a sleep time of 1 second to reduce CPU usage
