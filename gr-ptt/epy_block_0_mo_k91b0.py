"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pyfirmata
import time

from pyfirmata import util



board = pyfirmata.Arduino('/dev/ttyACM0') #"connects" the board to this code

it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:1:i')
digital_output = board.get_pin('d:13:o')
led = board.get_pin('d:11:p')


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""
    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
		gr.sync_block.__init__(self, name='Arduino Try',   # will show up in GRC
		in_sig=[np.float32],
        out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
		self.example_param = example_param

	def work(self, input_items, output_items):
        """example: multiply with constant"""
		if self.zeroInput(input_items):
			led.write(1)
		print(input_items[0])
		digital_output.write(1)
    	#time.sleep(1)
    	#digital_output.write(0)
    	#time.sleep(1)
		time.sleep(0.01)
		output_items[0][:] = input_items[0] * self.example_param
		return len(output_items[0])
        
        
        
	def zeroInput(self, input_items):
		for i in range(len(input_items[0])):
			if input_items[0][i]!=0:
				return False
		return True





    
