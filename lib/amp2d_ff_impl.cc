/* -*- c++ -*- */
/* 
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */
#include <iostream>
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "amp2d_ff_impl.h"

namespace gr {
  namespace vlp2 {

    amp2d_ff::sptr
    amp2d_ff::make(float Ax, float Dz, float m, std::vector<float> CtCr, float A, float R, float Ts, float n, float fov, float tx_number)
    {
      return gnuradio::get_initial_sptr
        (new amp2d_ff_impl(Ax, Dz, m, CtCr, A, R, Ts, n, fov, tx_number));
    }

    /*
     * The private constructor
     */
    amp2d_ff_impl::amp2d_ff_impl(float Ax, float Dz, float m, std::vector<float> CtCr, float A, float R, float Ts, float n, float fov, float tx_number)
      : gr::sync_block("amp2d",
              gr::io_signature::make(1, -1, sizeof(float)),
              gr::io_signature::make(1, -1, sizeof(float))
              )
  {
   	set_Ax(Ax);
        set_Dz(Dz);
        set_m(m);
        set_CtCr(CtCr, A, R, Ts, n, fov);
        set_C();
        
    }
    /*
     * Our virtual destructor.
     */
    amp2d_ff_impl::~amp2d_ff_impl()
    {
    }

    int
    amp2d_ff_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
        {     
    {}
       
      
      int ninputs = input_items.size();
      float **out = (float **) &output_items[0];
      for (int i = 0; i < noutput_items; i++){    
        for (int j = 0; j < ninputs; j++) {      	
         *out[j] =  sqrt(pow(amp2d_ff_impl::d_C[j] / ((float *) input_items[j])[i], 1/(amp2d_ff_impl::d_m + 3)));
          out[j]++; 		
      }
      }
           
 
      return noutput_items;
    }

  } /* namespace vlp2 */
} /* namespace gr */






