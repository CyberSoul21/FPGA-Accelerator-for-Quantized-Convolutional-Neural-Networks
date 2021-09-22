import serial
import time

import numpy as np

delay = 0.01



ser = serial.Serial('/dev/ttyUSB0')  # open serial port
ser.baudrate = 115200
print(ser.name)         # check which port was really used


img = [0,-1,122,-3,4,-50,6,-171,8,-9];

#img = np.asarray(img);

pos = 0;
neg = 1;

#ser.open()
#ser.write(str(chr(130)).encode("latin1"));

for x in range(0,len(img)):
	#print(img[x])
	if(img[x] >= 0):
		ser.write(str(chr(img[x])).encode("latin1"));
		ser.write(str(chr(pos)).encode("latin1"));

	if(img[x] < 0):
		ser.write(str(chr(img[x]*-1)).encode("latin1"));
		ser.write(str(chr(neg)).encode("latin1"));		
	line = ser.readline()   # read a '\n' terminated line
	print(line)

ser.close()             # close port


