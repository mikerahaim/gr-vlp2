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

#ifndef INCLUDED_VLP2_AMP2D_FIXED_HEIGHT_IMPL_H
#define INCLUDED_VLP2_AMP2D_FIXED_HEIGHT_IMPL_H

#include <vlp2/amp2d_fixed_height.h>

namespace gr {
  namespace vlp2 {

    class amp2d_fixed_height_impl : public amp2d_fixed_height
    {
     private:
      float d_Ax;
      float d_Dz;
      float d_m;
      float d_CtCr;
      float d_C;

     public:
      amp2d_fixed_height_impl(float Ax, float Dz, float m, float CtCr, float A, float R, float Ts, float n, float fov);
      ~amp2d_fixed_height_impl();

      void set_Ax(float Ax)     { d_Ax   = Ax;   }
      void set_Dz(float Dz)     { d_Dz   = Dz;   }
      void set_m(float m)       { d_m    = m;    }
      void set_CtCr(float CtCr) { d_CtCr = CtCr; }
      void set_C() { d_C = d_Ax * d_CtCr * (d_m+1)/(2*M_PI) * pow(d_Dz,d_m+1); }
      
      float Ax()   { return d_Ax;   }
      float Dz()   { return d_Dz;   }
      float m()    { return d_m;    }
      float CtCr() { return d_CtCr; }
      float C()    { return d_C;    }
      
      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace vlp2
} // namespace gr

#endif /* INCLUDED_VLP2_AMP2D_FIXED_HEIGHT_IMPL_H */

