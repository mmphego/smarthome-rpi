import smbus
import time
import sys
import serial

#print 'Number of arguments:', len(sys.argv), 'arguments.'

BAUD = 9600
try:
    serial_com = serial.Serial('/dev/ttyACM0', BAUD)
except serial.SerialException:
    serial_com = serial.Serial('/dev/ttyACM1', BAUD)
serial_com.close()
serial_com.open()
var = str(sys.argv[1])
#time.sleep(0.2)
serial_com.write(var)

#serial_com.write('1')
#time.sleep(0.5)
#serial_com.write('2')
#time.sleep(0.5)
#serial_com.write('3')
#time.sleep(0.5)
#serial_com.write('4')
#time.sleep(0.5)
#serial_com.write('5')
#time.sleep(0.5)
#serial_com.write('6')
