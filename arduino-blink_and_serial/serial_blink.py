import time
import serial
from serial_read import get_port
from serial_read import print_serial
from delay import get_delay

PORT = get_port() #this fits mac, for windows it's usually "COM3"
BAUD_RATE = 9600
TIMEOUT = 0.2
DELAY = get_delay()
arduino = serial.Serial(PORT, BAUD_RATE, timeout=TIMEOUT)

HIGH = b'1'
LOW = b'0'

print("connected on port:" , PORT)

while True:
	
	arduino.write(HIGH)
	#print_serial(arduino)
	
	time.sleep(DELAY)
	
	arduino.write(LOW)
	#print_serial(arduino)
	
	time.sleep(DELAY)