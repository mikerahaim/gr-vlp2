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
from ctcr_ff import ctcr_ff

class qa_ctcr_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data = (.1636, .1652, .1712, .1488)
        expected_result = (1.38816, 1.4017393, 1.45265018, 1.262583)
        src = blocks.vector_source_f(src_data)
        #Ptx, lamb_order, Htx, Hrx
        ctcr = ctcr_ff(.7, 1, 1.375, 0,1)
        snk = blocks.vector_sink_f()
        self.tb.connect(src, ctcr)
        self.tb.connect(ctcr, snk)
        self.tb.run()
        result_data = snk.data()
        print("Expected Results")
        print(expected_result)
        print("Calculated results")
        print(result_data)
        # check data
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 4)


if __name__ == '__main__':
    gr_unittest.run(qa_ctcr_ff, "qa_ctcr_ff.xml")
