#!/usr/bin/python2
import socket
import os
import time

sock = socket.socket(socket.AF_INET,   # Internet
    socket.SOCK_DGRAM)    # UDP
sock.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
UDP_IP = sock.getsockname()[0]
UDP_PORT = 5005

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
    print "received message:", data
    if data == "kitchen on" or data ==  "kitchen off":
        os.system("home_auto 1 > /dev/null 2>&1");

        #if data ==  "Kitchen Light Off":
        #       os.system("home_auto 1 > /dev/null 2>&1")

    elif data == "dining on" or data == "dining off":
        os.system("home_auto 2 > /dev/null 2>&1");

    elif data == "bedroom on" or data == "bedroom off":
                os.system("home_auto 3 > /dev/null 2>&1");

    elif data == "tv room on" or data == "tv room off":
                os.system("home_auto 4 > /dev/null 2>&1");

    elif data == "everything on" or data == "everything off":
                os.system("home_auto 5 > /dev/null 2>&1");

    else :
        print "invalid parameter"

    time.sleep(1)
#    break
    #continue
