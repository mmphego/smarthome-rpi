#!/usr/bin/python2
# Purpose of this script is to ping a certain static IP(android mobile) is destination is
# reachable set a  gpio pin and activate flite(voice response) else if it not detected
# gpio will remain off
# Created by Mpho Mphego (mpho112@gmail.com)
# http://pastebin.com/nLkaZ308

import time
import subprocess

mac_address = 'bc:6e:64:df:d7:d9'
mob_ip = None
while True:
    process = subprocess.Popen(
        'sudo arp-scan --interface wlan0 -l | grep {} | cut -f 1'
            .format(mac_address), shell=True, stdout=subprocess.PIPE, )
    mob_ip = process.communicate()[0].strip()
    if mob_ip != '':
        break

while True:  # Setup a while loop to wait for a button press
    if subprocess.call(['ping -c1 {}'.format(mob_ip)],
        shell=True, stdout=open('/dev/null', 'w')) == 0:
        print "host is detected"
    else:
        print "host unreachable"
    break
