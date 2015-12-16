#!/usr/bin/python2
import socket
import time
import serial
import numpy as np

from logger import LOGGER

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
# Getting systems IP
UDP_IP = sock.getsockname()[0]
UDP_PORT = 5005
nbytes = 1024
time_out = 300
sleep_time = 0.01

# Range 30 - 60
sensitivity = 30
limit = 270
# Low pass filter RC time constant
alpha = 0.1
x_data, y_data, z_data = [None] * 3

baud = 9600
arduino_output = {'relay1_on_off': 1, 'relay1_off': 10, 'relay1_on': 11,
                  'relay2_off': 20, 'relay2_on': 21, 'relay3_off': 30,
                  'relay3_on': 31, 'relay4_off': 40, 'relay4_on': 41,
                  'relay5_off': 50, 'relay5_on': 51
                  }
locals().update(arduino_output)

#try:
    #serial_comm = serial.Serial('/dev/ttyACM0', baud)
#except serial.SerialException:
    #serial_comm = serial.Serial('/dev/ttyACM1', baud)

try:
    LOGGER.info("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))
    print("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))
    LOGGER.info("Connected to host.")
    print("Connected to host.")
except Exception as e:
    LOGGER.error('Unable to start UDP sockets due to {}.'.format(e))
    sock.close()
    raise RuntimeError('Unable to start UDP sockets due to {}.'.format(e))


def gesture_control():
    print 'Accelerometer: ',data
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
            LOGGER.info('Mobile Shaken')
            print 'Mobile shaken'
            #serial_comm.write(relay1_on_off)


def voice_recognition(data):
    # TODO MM  2015/11/04
    # insert code here to switch on lights

    if data == "bedroom light on" or data == "bedroom on":
        #serial_comm.write(relay1_on)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "bedroom light off" or data == "bedroom off":
        #serial_comm.write(relay1_off)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "kitchen light on" or data == "kitchen on":
        #serial_comm.write(relay2_on)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "kitchen light off" or data == "kitchen off":
        #serial_comm.write(relay2_off)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "dining light on" or data == "dining light off":
        #serial_comm.write(relay3_on)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "dining light off" or data == "dining off":
        #serial_comm.write(relay3_off)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "tv room light on" or data == "tv room light off":
        #serial_comm.write(relay4_on)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "tv room light off" or data == "tv room off":
        #serial_comm.write(relay4_off)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "all lights on" or data == "lights on":
        #serial_comm.write(relay5_on)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "all lights off" or data == "lights off":
        #serial_comm.write(relay5_off)
        print data
        LOGGER.info('Data: {}'.format(data))

    else:
        print "invalid parameter: ", data


while True:
    # TODO MM 2015/11/04
    # Combine gesture control and voice recognition
    # buffer size is 1024 bytes
    data, addr = sock.recvfrom(nbytes)
    # format
    # data : str containing list
    # addr : 'xxx.xxx.xxx.xxx'
    # print 'data length', len(data)
    try:
        eval(data)
        gesture_control()
    except Exception:
        voice_recognition(data)
