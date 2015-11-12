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

# Range 30 - 60
sensitivity = 25
limit = 270
# RC time constant
alpha = 0.1
x_data, y_data, z_data = [None] * 3

LOGGER.info("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))
print("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))
try:
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))
    # sock.settimeout(5)
    LOGGER.info("Connected to host.")
    print("Connected to host.")
except Exception as e:
    LOGGER.error('Unable to start UDP sockets due to {}.'.format(e))
    sock.close()
    raise RuntimeError('Unable to start UDP sockets due to {}.'.format(e))


def notification():
    """
    :rtype : None
    """
    LOGGER.info('Mobile Shaken')
    # call switch relay or whatever here


def gesture_control():
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
        print Prev_Acc
        if Prev_Acc >= sensitivity <= limit:
            notification()
            print 'Mobile shaken'

def voice_recognition():
    # TODO MM  2015/11/04
    # insert code here to switch on lights
    """

    :rtype : None
    """
    pass

while True:
    # TODO MM 2015/11/04
    # Combine gesture control and voice recognition
    # buffer size is 1024 bytes
    data, addr = sock.recvfrom(1024)
    # format
    # data : str containing list
    # addr : 'xxx.xxx.xxx.xxx'
    #import IPython;IPython.embed()
    if len(eval(data)) == 3:
        #print data
        gesture_control()
    if len(eval(data)) == 1:
        print data
        import IPython;IPython.embed()

        voice_recognition()
