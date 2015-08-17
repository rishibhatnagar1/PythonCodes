import serial
ser = serial.Serial('/dev/tty.usbmodem1451',9600)

while True:
	print ser.readline()
