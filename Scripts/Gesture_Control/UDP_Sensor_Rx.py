#!/usr/bin/python2
import socket
import time
import serial
import numpy as np
import subprocess
import sys

from logger import LOGGER
sys.path.insert(1, '/home/pi/Scripts/Relay_Control/')
from relay_control import *


sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
# Getting systems IP
UDP_IP = sock.getsockname()[0]
UDP_PORT = 5005

rst_counter = 0

nbytes = 1024
sleep_time = 0.01

# Range 30 - 60
sensitivity = 30
limit = 270
max_limit = float(sensitivity + limit + 100)

# Low pass filter RC time constant
alpha = 0.1
x_data, y_data, z_data = [None] * 3


try:
    LOGGER.info("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))
    print("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    #sock.bind((UDP_IP, UDP_PORT))
    sock.bind(('', UDP_PORT))
    LOGGER.info("Connected to host.")
    print("Connected to host.")

except Exception as e:
    LOGGER.error('Unable to start UDP sockets due to {}.'.format(e))
    sock.close()
    raise RuntimeError('Unable to start UDP sockets due to {}.'.format(e))

def relay_off(pin):
    subprocess.check_call([gpio_control, 'write', '{}'.format(pin), '1'])
    #return False

def relay_on(pin):
    subprocess.check_call([gpio_control, 'write', '{}'.format(pin), '0'])
    #return True

def gesture_switch_on():
    global rst_counter
    rst_counter += 1
    relay_on(Relay1)

def gesture_switch_off():
    global rst_counter
    rst_counter = 0
    relay_off(Relay1)

def gesture_control():
    #print 'Accelerometer: ',data
    x_data, y_data, z_data = eval(data)
    # Sleep for every samples.
    time.sleep(sleep_time)
    Current_Acc = 0.0
    Prev_Acc = 0.0
    if x_data is not None:
        # https://en.wikipedia.org/wiki/Low-pass_filter
        # simple Low pass filter algorithm
        Last_Acc = Current_Acc
        Current_Acc = np.abs((float(x_data ** 2 + y_data ** 2 + z_data ** 2)))
        delta = Current_Acc - Last_Acc
        Prev_Acc = Prev_Acc + alpha * delta
        if Prev_Acc >= sensitivity <= limit:
            LOGGER.info ('Mobile Shaken: Relay ON')
            print ('Mobile Shaken: Relay ON')
            gesture_switch_on()
            if rst_counter > 1:
                LOGGER.info ('Mobile Shaken: Relay OFF')
                print ('Mobile Shaken: Relay OFF')
                gesture_switch_off()

def voice_recognition(data):
    if data == "bedroom light on" or data == "bedroom on":
        relay_on(relay1)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "bedroom light off" or data == "bedroom off":
        relay_off(relay1)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "kitchen light on" or data == "kitchen on":
        relay_on(relay2)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "kitchen light off" or data == "kitchen off":
        relay_off(relay2)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "dining light on" or data == "dining light off":
        relay_on(relay3)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "dining light off" or data == "dining off":
        relay_on(relay3)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "tv room light on" or data == "tv room light off":
        relay_on(relay4)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "tv room light off" or data == "tv room off":
        relay_off(relay4)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "all lights on" or data == "lights on":
        for relay, gpio in relays_conf.iteritems():
            relay_on(gpio)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "all lights off" or data == "lights off":
        for relay, gpio in relays_conf.iteritems():
            relay_off(gpio)
        print data
        LOGGER.info('Data: {}'.format(data))

    else:
        print "invalid parameter: ", data

while True:
    data, addr = sock.recvfrom(nbytes)
    """ format
        data : str containing list
        addr : 'xxx.xxx.xxx.xxx'
        print 'data length', len(data)
    """
    try:
        eval(data)
        gesture_control()
    except Exception:
        voice_recognition(data)
