import serial
ser=serial.Serial()
ser.timeout=3
ser.baudrate=9600
ser.port='/dev/ttyAMA0'
ser.open()
ser.write('AT\r\n')
ser.readlines()
ser.write('AT+RST\r\n')
ser.readlines()
ser.write('AT+CWLAP\r\n')
ser.readlines()
ser.write('AT+CWMODE=3\r\n')
ser.readlines()
ser.close()
