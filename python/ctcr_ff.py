#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class ctcr_ff(gr.sync_block):
    """
    docstring for block ctcr_ff
    """
    def __init__(self, Ptx, lamb_order, Htx, Hrx, RX_area):
    	self.Ptx=Ptx
    	self.lamb_order=lamb_order
    	self.RX_area=RX_area
    	#This assumes that the transmitter is higher than receiver
    	self.dsquared = numpy.power(Htx-Hrx, 2)
    	
        gr.sync_block.__init__(self,
            name="ctcr_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = (in0/self.Ptx)*(2*numpy.pi*self.dsquared)/((self.lamb_order+1)*(self.RX_area))
        return len(output_items[0])

