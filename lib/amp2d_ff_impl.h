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

#ifndef INCLUDED_VLP2_AMP2D_FF_IMPL_H
#define INCLUDED_VLP2_AMP2D_FF_IMPL_H

#include <vlp2/amp2d_ff.h>

namespace gr {
  namespace vlp2 {

    class amp2d_ff_impl : public amp2d_ff
    {
     private:
      float d_Ax;
      float d_Dz;
      float d_m;
      std::vector<float> d_CtCr;
      std::vector<float> d_C;
      float d_tx_number;
      
      
		//Ax is amplitude of signal, Dz is height, m is Lambertian Order, CtCr is the Tx_Rx gain constant, A is area of the receiver, Ts is filter transmittance, n is the concentrator, fov is field of view
     public:
      amp2d_ff_impl(float Ax, float Dz, float m, std::vector<float> CtCr, float A, float R, float Ts, float n, float fov, float tx_number);
      ~amp2d_ff_impl();
      
      void set_Ax(float Ax)     { d_Ax   = Ax;   }
      void set_Dz(float Dz)     { d_Dz   = Dz;   }
      void set_m(float m)       { d_m    = m;    }
      void set_CtCr(std::vector<float> CtCr, float A, float R, float Ts, float n, float fov) { 
      		for (int i = 0; i < CtCr.size(); i++){
      d_CtCr.push_back(CtCr[i]*A*R*Ts*pow(n,2)/pow(sin(M_PI*fov/180),2)); 
      		}
      		}      		 
      			
      void set_C() { for (int i = 0; i < d_CtCr.size(); i++)
      {   
      	d_C.push_back(d_Ax * d_CtCr[i] * (d_m+1)/(2*M_PI) * pow(d_Dz,d_m+1));
      	}}
      void set_tx_number( float tx_number ) { d_tx_number = tx_number; }
      float Ax()   { return d_Ax;   }
      float Dz()   { return d_Dz;   }
      float m()    { return d_m;    }
      std::vector<float> CtCr() { return d_CtCr; }
      std::vector<float> C()    { return d_C;    }
      float tx_number() { return d_tx_number; }
      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace vlp2
} // namespace gr

#endif /* INCLUDED_VLP2_AMP2D_FF_IMPL_H */

