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

#ifndef INCLUDED_VLP2_TRILAT_SCALEABLE_FF_IMPL_H
#define INCLUDED_VLP2_TRILAT_SCALEABLE_FF_IMPL_H

#include <vlp2/trilat_scaleable_ff.h>

namespace gr {
  namespace vlp2 {

    class trilat_scaleable_ff_impl : public trilat_scaleable_ff
    {
     private:
      // Nothing to declare in this block.

     public:
     std::vector<std::vector<float> > d_tx_coords;
     float d_tx_number;
     float d_tx_z;
     //static const float d_A[3*d_tx_number-1]; //array of floats to hold coefficients in
     std::vector<float> d_sqrd_x_1;
     std::vector<float> d_reference;
     
      void set_tx_coords ( std::vector<std::vector<float> > tx_coords ) {d_tx_coords = tx_coords; }
      void set_tx_z (float tx_z) {d_tx_z = tx_z;}
      void set_tx_number (float tx_number) {d_tx_number = tx_number;}
      void set_sqrd_x_1 (std::vector< std::vector<float> > tx_coords) {
		std::vector<float> reference = tx_coords[0];
     		std::vector<float> beacon_coords;
      		for (int i = 1; i < tx_coords.size(); i++){
      		//each value in sqrd_x_1 is the squared distance between the beacon i and the reference point
      		beacon_coords = tx_coords[i];     		
      	    d_sqrd_x_1.push_back( pow(beacon_coords[0] - reference[0], 2) + pow(beacon_coords[1] - reference[1],2) + pow(beacon_coords[1] - reference[1], 2) );    };            
      }
   
      void set_reference(std::vector< std::vector< float > > tx_coords) { d_reference = tx_coords[0]; }
      float reference(int i ) {return d_reference[i]; }
      std::vector< std::vector<float> > tx_coords() { return d_tx_coords; }
      float tx_number() { return d_tx_number; }
      float tx_z() { return d_tx_z; }
      std::vector< float> sqrd_x_1() { return d_sqrd_x_1; }
              
      trilat_scaleable_ff_impl(std::vector<std::vector<float> > tx_coords, float tx_number, float tx_z);
      ~trilat_scaleable_ff_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace vlp2
} // namespace gr

#endif /* INCLUDED_VLP2_TRILAT_SCALEABLE_FF_IMPL_H */

