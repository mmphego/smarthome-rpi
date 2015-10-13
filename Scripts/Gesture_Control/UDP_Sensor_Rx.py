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
Current_Acc = 0
Prev_Acc = 0
sensitivity = 80
limit = 270
# RC time constant
alpha = 0.1
x_data, y_data, z_data = [None] * 3

LOGGER.info("Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT))
try:
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))
    LOGGER.info("Connected to host.")
except Exception as e:
    LOGGER.error('Unable to start UDP sockets due to {}.'.format(e))
    raise RuntimeError('Unable to start UDP sockets due to {}.'.format(e))


def notification():
    """

    :rtype : None
    """
    LOGGER.info('Mobile Shaken')
    # call switch relay or whatever here


while True:
    # buffer size is 1024 bytes
    data, addr = sock.recvfrom(1024)
    x_data, y_data, z_data = eval(data)
    # Sleep for every samples.
    time.sleep(1e-2)
    if x_data is not None:
        # https://en.wikipedia.org/wiki/Low-pass_filter
        # simple Low pass filter algorithm
        Last_Acc = Current_Acc
        Current_Acc = np.abs((float(x_data ** 2 + y_data ** 2 + z_data ** 2)))
        delta = Current_Acc - Last_Acc
        Prev_Acc = Prev_Acc + alpha * delta
        if sensitivity <= Prev_Acc <= limit:
            notification()
