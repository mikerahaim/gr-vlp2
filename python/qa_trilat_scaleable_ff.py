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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import vlp2_swig as vlp2

class qa_trilat_scaleable_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        my_tx_number=4;
    	my_tx_coords=( (.75, .23, 1.355), (.25, .23, 1.355), (.25, .93, 1.355), (.75, .93, 1.355))
    	my_txz=1.355
        print "test begun"
        src_data1=(0.9505027,0.9505027,0.9505027)
        src_data2=(0.8148127, 0.8148127, 0.8148127)
        src_data3=(0.7446058, 0.7446058, 0.7446058)
        src_data4=(0.69849331, 0.69849331, 0.69849331)
        expected_resultx = (.42491,.42491,.42491)
        expected_resulty = (1.06672,1.06672,1.06672)
        expected_resultz = (1.355,1.355,1.355)
                     
        src1 = blocks.vector_source_f(src_data1)
        src2 = blocks.vector_source_f(src_data2)
        src3 = blocks.vector_source_f(src_data3)
        src4 = blocks.vector_source_f(src_data4)
        #src5 = blocks.vector_source_f(src_data5)
        blk = vlp2.trilat_scaleable_ff(my_tx_coords,my_tx_number,my_txz)        
        dstx = blocks.vector_sink_f()    
        dsty = blocks.vector_sink_f()
        dstz = blocks.vector_sink_f()
        
        print "blocks initialized"    
        self.tb.connect(src1, (blk,0))
        self.tb.connect(src2, (blk,1))
        self.tb.connect(src3, (blk,2))
        self.tb.connect(src4, (blk,3))
        #self.tb.connect(src5, (blk,4))      
        self.tb.connect((blk,0), dstx)
        self.tb.connect((blk,1), dsty)
        self.tb.connect((blk,2), dstz)
        self.tb.run()
        
        result_data1 = dstx.data()

  	print(result_data1)
  	result_data2 = dsty.data()
  	print(result_data2)
  	
        self.assertFloatTuplesAlmostEqual(expected_resultx, result_data1, 4)

if __name__ == '__main__':
    gr_unittest.run(qa_trilat_scaleable_ff, "qa_trilat_scaleable_ff.xml")
