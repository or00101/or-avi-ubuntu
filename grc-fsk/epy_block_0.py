"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import time
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, samp_rate=32000, f_c=1000, diviation=500):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='FSK MOD',   # will show up in GRC
            in_sig=[np.byte],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.f_c = f_c
        self.samp_rate = samp_rate
        self.diviation = diviation
        self._update_freq(0)
        self.theta = 0
        self.EPSILON = 0.001
    
    def _update_signal_var(self):
        self.theta += 2 * np.pi * self._freq / self.samp_rate
        self.theta %= 2 * np.pi
    
    def _update_freq(self, bit):
        if bit:
            self._freq = self.f_c + self.diviation
        else:
            self._freq = self.f_c - self.diviation
            
    def work(self, input_items, output_items):
        """example: multiply with constant"""
        for i in range(len(input_items[0])):
            if abs(self.theta) < self.EPSILON:
                self._update_freq(int(input_items[0][i]))
            output_items[0][i] = float(np.sin(self.theta))
            self._update_signal_var()
        #print(len(output_items[0]), time.time())
        return len(output_items[0])
