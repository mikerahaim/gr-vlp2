#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
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

class qa_amp2d_fixed_height (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        my_Ax = 1
        my_Dz = 1
        my_m = 1.5
        my_CtCr = 2
        my_A = 1
        my_R = 1
        my_Ts = 1
        my_n = 1
        my_fov = 90

        src_data = (1.0,2.0,3.0,4.0)
        expected_result = (0.9505027, 0.8148127, 0.7446058, 0.69849331)
        #expected_result = (0.97493728, 0.9026697624, 0.8629067157, 0.835758122)
        src = blocks.vector_source_f(src_data)
        blk = vlp2.amp2d_fixed_height(my_Ax,my_Dz,my_m,my_CtCr,my_A,my_R,my_Ts,my_n,my_fov)
        dst = blocks.vector_sink_f()
        print "CtCr: "
        print blk.CtCr();
        
        self.tb.connect(src, blk)
        self.tb.connect(blk, dst)
        self.tb.run()
        result_data = dst.data()
  
        self.assertFloatTuplesAlmostEqual(expected_result, result_data, 4)


if __name__ == '__main__':
    gr_unittest.run(qa_amp2d_fixed_height, "qa_amp2d_fixed_height.xml")
