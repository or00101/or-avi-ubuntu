import serial
import sys
import platform

def print_serial(arduino):
        res = ""
        temp = arduino.read().decode('utf-8')
        while temp:
                res += temp
                temp = arduino.read().decode('utf-8')

        if res:
                print(res.strip())

def _get_port_uno():
        if platform.system() == "Windows":
                return "COM3"
        elif platform.system() == "Darwin":
                return "/dev/cu.usbmodem14101"
        elif platform.system() == "Linux":
                return "/dev/ttyACM0"

def get_port():
        baord_type = sys.argv[1]
        print("Board type:", sys.argv[1])
        if baord_type == "uno":
                return _get_port_uno()
        if baord_type == "nano":
                return "/dev/cu.usbserial-1410" #work only on mac for now... (due to my laziness...)

if __name__ == '__main__':
	PORT = get_port() #this fits mac, for windows it's usually "COM3"
	BAUD_RATE = 9600
	TIMEOUT = 0.2
	arduino = serial.Serial(PORT, BAUD_RATE, timeout=TIMEOUT)
	while True:
		print_serial(arduino)
