#!/usr/bin/python2
# Purpose of this script is to ping a certain static IP(android mobile) is destination is
# reachable set a  gpio pin and activate flite(voice response) else if it not detected
# gpio will remain off
# Created by Mpho Mphego (mpho112@gmail.com)
# http://pastebin.com/nLkaZ308
import os
import subprocess
from logger import LOGGER

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
    count = 0
    if subprocess.call(['ping -c1 {}'.format(mob_ip)],
                       shell=True, stdout=open('/dev/null', 'w')) == 0:
        count += 1
        if count > 3:
            count = 0
            LOGGER.info("Mobile detected: IP ", mob_ip)
            subprocess.Popen('mpg123 Welcome_Home.mp3', shell=True, stdout=subprocess.PIPE,)
            # TODO MM 2015/11/04
            # Switch on lights

            break
