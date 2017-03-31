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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "trilat_scaleable_ff_impl.h"

namespace gr {
  namespace vlp2 {

    trilat_scaleable_ff::sptr
    trilat_scaleable_ff::make(std::vector<std::vector<float> > tx_coords, float tx_number, float tx_z)
    {
      return gnuradio::get_initial_sptr
        (new trilat_scaleable_ff_impl(tx_coords, tx_number, tx_z));
    }

    /*
     * The private constructor
     */
    trilat_scaleable_ff_impl::trilat_scaleable_ff_impl(std::vector<std::vector<float> > tx_coords, float tx_number, float tx_z)
      : gr::sync_block("trilat_scaleable_ff",
              gr::io_signature::make(3, -1, sizeof(float)),
              gr::io_signature::make(3, 3, sizeof(float)))
    {  set_tx_number(tx_number);
       set_tx_coords(tx_coords);
       set_tx_z(tx_z);
       set_sqrd_x_1(tx_coords);
       set_reference(tx_coords);
       //set_A(tx_coords);
    }

    /*
     * Our virtual destructor.
     */
    trilat_scaleable_ff_impl::~trilat_scaleable_ff_impl()
    {
    }

    int
    trilat_scaleable_ff_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    { 
    
      int txn = static_cast<int>(trilat_scaleable_ff_impl::tx_number());
      std::vector<float> beacon_coords; 
      std::vector<std::vector<float> > coords = trilat_scaleable_ff_impl::tx_coords();        
      Eigen::MatrixX3f Ax;  
      Ax.resize(txn-1,3);
       	for (int i = 0; i < txn-1; i++) {     		
       		beacon_coords=coords[i+1];
       		Ax(i,0) = beacon_coords[0] - trilat_scaleable_ff_impl::reference(0);
       		Ax(i,1) = beacon_coords[1] - trilat_scaleable_ff_impl::reference(1);
       		Ax(i,2) = beacon_coords[2] - trilat_scaleable_ff_impl::reference(2);}       		
      Eigen::Matrix<float, Eigen::Dynamic, 1> Bx; Bx.resize(txn-1,1);
      //std::cout << "Matrix A: " << Ax << std::endl;
      float **out = (float **) &output_items[0];   
        for (int i = 0; i < noutput_items; i++){    
        for (int j = 1; j < txn; j++) {   
           Bx(j-1) =   .5*( ( ((float *)input_items[0])[i]*((float *)input_items[0])[i]) - ( ((float *)input_items[j])[i]*((float *)input_items[j])[i]) + trilat_scaleable_ff_impl::d_sqrd_x_1[j-1] );
        } 
        
         //std::cout << "Matrix B: " << Bx << std::endl;
         
	 Eigen::Vector3f pos = Ax.colPivHouseholderQr().solve(Bx);
	 //std::cout << "LstSquares Solution of Ax=B" << std::endl << pos << std::endl;
      	*out[0]= pos(0,0)+reference(0); *out[1]= pos(1,0)+reference(1) ; *out[2]= pos(2,0);
      	  out[0]++; out[1]++; out[2]++;
      	}
        
      return noutput_items;
    }

  } /* namespace vlp2 */
} /* namespace gr */

