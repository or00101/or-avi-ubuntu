import sys

def get_delay():
	""" 
		 This gives you the option to set the delay\
	 	 yourself by running this script: python3 serial_blink.py <delay>  
	"""
	
	if len(sys.argv) == 3:
		delay = float(sys.argv[2])
	else:
		delay = 0.5

	print("Delay:", delay)

	return delay