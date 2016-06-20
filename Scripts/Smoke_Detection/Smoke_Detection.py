import smbus
import time
import sys
import serial
import subprocess
from os import devnull

def disable_serial_rst():
    dev_null = open(devnull, 'w')
    for i in range(2):
        subprocess.Popen(
            'stty -F /dev/ttyACM{} -hupcl'
            .format(i), shell=True, stdout=dev_null,stderr=dev_null, ).communicate()
    return True

disable_serial_rst()

BAUD = 9600

try:
    serial_com = serial.Serial('/dev/ttyACM0', BAUD)
    serial_com.close()
    serial_com.open()
except serial.SerialException:
    try:
        serial_com = serial.Serial('/dev/ttyACM1', BAUD)
        serial_com.close()
        serial_com.open()
    except serial.SerialException:
        serial_com = None

def get_gas_sensor():
    try:
        sensor = serial_com.readline().startswith('Sensor')
    except:
        return 0
    if sensor:
        sensor_val = serial_com.readline().strip().split()
        if len(sensor_val) == 3:
            return int(sensor_val[-1])

#print get_gas_sensor()
