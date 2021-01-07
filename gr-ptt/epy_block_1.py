"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import time
import pyfirmata
from pyfirmata import util

class Amp_Driver:
    def __init__(self, arduino_do_pin):
        arduino = pyfirmata.Arduino(self.get_com_port())
        self.it = pyfirmata.util.Iterator(arduino)
        self.it.start()

        self.digital_output = arduino.get_pin(f"d:{str(arduino_do_pin)}:o")

    def get_com_port(self):
        return '/dev/ttyACM0'

    def wake_up(self):
        self.digital_output.write(0)

    def shut_down(self):
        self.digital_output.write(1)

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""
    def __init__(self, arduino_pin=12):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(self, name='Arduino Driver embedded block',   # will show up in GRC
        in_sig=[np.float32],
        out_sig=[np.float32]
        )

        self.amp_driver = Amp_Driver(arduino_pin)
        

    def work(self, input_items, output_items):
        if self.is_input_all_zeros(input_items):
            self.amp_driver.shut_down()
            output_items[0][:] = 0 # When debugging this will allow us to plug this block's output  to a time sink and see if and when the driver woke up
        else:
            self.amp_driver.wake_up()
            output_items[0][:] = 1 # When debugging this will allow us to plug this block's output to a time sink and see if and when the driver shut down

        return len(output_items[0])

    def is_input_all_zeros(self, input_items):
        for i in range(len(input_items[0])):
            if input_items[0][i]!=0:
                return False
        return True


