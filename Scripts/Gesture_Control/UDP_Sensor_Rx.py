#!/usr/bin/python2
import socket
import time
import numpy as np

from logger import LOGGER

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
# Getting systems IP
UDP_IP = sock.getsockname()[0]
UDP_PORT = 5005
LOGGER.info("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))
print("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))

# Range 30 - 60
sensitivity = 25
limit = 270
max_limit = float(sensitivity + limit + 100)
# Low pass filter RC time constant
alpha = 0.1
x_data, y_data, z_data = [None] * 3

baud = 9600
arduino_output = {'relay1_off' : '2',
                  'relay1_on'  : '1',
                  'relay2_off' : '4',
                  'relay2_on'  : '3',
                  'relay3_off' : '6',
                  'relay3_on'  : '5',
                  'relay4_off' : '8',
                  'relay4_on'  : '7'
                  }
locals().update(arduino_output)

try:
    serial_comm = serial.Serial('/dev/ttyACM0', baud, timeout=10)
except serial.SerialException:
    serial_comm = serial.Serial('/dev/ttyACM1', baud, timeout=10)

try:
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(30)
    LOGGER.info("Connected to host.")
    print("Connected to host.")
except Exception as e:
    LOGGER.error('Unable to start UDP sockets due to {}.'.format(e))
    sock.close()
    raise RuntimeError('Unable to start UDP sockets due to {}.'.format(e))


def gesture_control():
    #print 'Accelerometer: ',data
    x_data, y_data, z_data = eval(data)
    # Sleep for every samples.
    time.sleep(1e-2)
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
            LOGGER.info('Mobile Shaken Relay On')
            print ('Mobile Shaken Relay On')
            serial_comm.write(relay1_on)
        #ToDo: read log file, if shaken before twice ,3rd time will go off



def voice_recognition():
    # TODO MM  2015/11/04
    # insert code here to switch on lights
    if data == "kitchen light on" or data == "kitchen light off":
        import IPython;IPython.embed()
        serial_comm.write(relay1_on)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "bedroom light off" or data == "bedroom off":
        serial_comm.write(relay1_off)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "kitchen light on" or data == "kitchen on":
        serial_comm.write(relay2_on)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "kitchen light off" or data == "kitchen off":
        serial_comm.write(relay2_off)
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "dining light on" or data == "dining light off":
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "bedroom light on" or data == "bedroom light off":
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "tv room light on" or data == "tv room light off":
        print data
        LOGGER.info('Data: {}'.format(data))

    elif data == "all lights on" or data == "all lights on":
        print data
        LOGGER.info('Data: {}'.format(data))

    else:
        print "invalid parameter"


while True:
    # TODO MM 2015/11/04
    # Combine gesture control and voice recognition
    # buffer size is 1024 bytes
    data, addr = sock.recvfrom(1024)
    # format
    # data : str containing list
    # addr : 'xxx.xxx.xxx.xxx'
    print len(data)
    if len(data) > 50:
        gesture_control()
    else:
        print data
        voice_recognition()
