#!/usr/bin/python
import time
import sys
import subprocess

from yamlConfigFile import configFile

relays_conf = configFile()['RelaysSetup']
locals().update(relays_conf)
gpio_control = '/usr/local/bin/gpio'

for relay, gpio in relays_conf.iteritems():
    subprocess.check_call([gpio_control, 'mode', '{}'.format(gpio), 'out'])


def relay_off(pin):
    subprocess.check_call([gpio_control, 'write', '{}'.format(pin), '1'])

def relay_on(pin):
    subprocess.check_call([gpio_control, 'write', '{}'.format(pin), '0'])
