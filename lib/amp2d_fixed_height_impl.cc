/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "amp2d_fixed_height_impl.h"

namespace gr {
  namespace vlp2 {

    amp2d_fixed_height::sptr
    amp2d_fixed_height::make(float Ax, float Dz, float m, float CtCr, float A, float R, float Ts, float n, float fov)
    {
      return gnuradio::get_initial_sptr
        (new amp2d_fixed_height_impl(Ax, Dz, m, CtCr, A, R, Ts, n, fov));
    }

    /*
     * The private constructor
     */
    amp2d_fixed_height_impl::amp2d_fixed_height_impl(float Ax, float Dz, float m, float CtCr, float A, float R, float Ts, float n, float fov)
      : gr::sync_block("amp2d_fixed_height",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {
        set_Ax(Ax);
        set_Dz(Dz);
        set_m(m);
        set_CtCr(CtCr*A*R*Ts*pow(n,2)/pow(sin(M_PI*fov/180),2));
        set_C();
    }

    /*
     * Our virtual destructor.
     */
    amp2d_fixed_height_impl::~amp2d_fixed_height_impl()
    {
    }

    int
    amp2d_fixed_height_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      
      for (int i = 0; i < noutput_items; i++) {
        out[i] = pow(amp2d_fixed_height_impl::d_C / in[i], 1/(amp2d_fixed_height_impl::d_m + 3));
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace vlp2 */
} /* namespace gr */

