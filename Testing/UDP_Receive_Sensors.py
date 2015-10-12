#!/usr/bin/python2
import socket
import os
import time
import numpy as np
#from logger  import LOGGER

sock = socket.socket(socket.AF_INET,   # Internet
    socket.SOCK_DGRAM)    # UDP
sock.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
UDP_IP = sock.getsockname()[0]
UDP_PORT = 5005
Current_Acc =0
mAccel=0
x_data, y_data, z_data = [0]*3
print "Listening on IP:{}:{} ".format(UDP_IP, UDP_PORT)
try:
    sock = socket.socket(socket.AF_INET, # Internet
        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    print "UDP Ready to Receive!"
except:
    raise RuntimeError('Unable to start UDP')

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print 'received message:', data
    x_data, y_data, z_data = eval(data)
    #print 'X_data:{}'.format(x_data)
    #print 'Y_data:{}'.format(y_data)
    #print 'Z_data:{}\n'.format(z_data)
    time.sleep(.1)
    if x_data != None:
        Last_Acc = Current_Acc
        Current_Acc = np.abs(np.sqrt(float(x_data**2 + y_data**2 + z_data**2)))
        delta = Current_Acc - Last_Acc
        mAccel = mAccel*.9 + delta
        print mAccel
        #import IPython;IPython.embed()
