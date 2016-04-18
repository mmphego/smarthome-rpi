#!/usr/bin/python2
# Purpose of this script is to ping a certain static IP(android mobile) is destination is
# reachable set a  gpio pin and activate flite(voice response) else if it not detected
# gpio will remain off
# Created by Mpho Mphego (mpho112@gmail.com)
# http://pastebin.com/nLkaZ308
import os
import subprocess
import time
import yaml
from logger import LOGGER
from yamlConfigFile import configFile

try:
    mac_address = configFile()['PresenceDetector']['macaddress']
    if mac_address == str():
        raise KeyError
except KeyError:
    mac_address = 'bc:6e:64:df:d7:d9'

def get_ip(mac_add):
    mob_ip = None
    while True:
        process = subprocess.Popen(
            'sudo arp-scan --interface wlan0 -l | grep {} | cut -f 1'
                .format(mac_add), shell=True, stdout=subprocess.PIPE, )
        mob_ip = process.communicate()[0].strip()
        time.sleep(.5)
        if mob_ip != '':
            break
    return mob_ip

def ping_mob_ip(mobile_ip):
    dev_null = open(os.devnull, 'w')
    if mobile_ip is not None:
        count = 0
        while True:  # Setup a while loop to wait for a button press
            time.sleep(.5)
            if subprocess.call(['ping -c1 {}'.format(mobile_ip)],
                               shell=True,
                               stdout=dev_null,
                               stderr=subprocess.STDOUT) == 0:
                count += 1
                if count > 2:
                    print 'Mobile detected'
                    LOGGER.info("Mobile detected: IP, {}".format(mobile_ip))
                    #subprocess.Popen('mpg123 Welcome_Home.mp3', shell=True, stdout=subprocess.PIPE,)
                    # TODO MM 2015/11/04
                    # Switch on lights
                    count = 0
                    break
        return True

ping_mob_ip(get_ip(mac_address))
