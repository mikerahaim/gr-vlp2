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


#ifndef INCLUDED_VLP2_AMP2D_FF_H
#define INCLUDED_VLP2_AMP2D_FF_H

#include <vlp2/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace vlp2 {

    /*!
     * \brief <+description of block+>
     * \ingroup vlp2
     *
     */
    class VLP2_API amp2d_ff : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<amp2d_ff> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of vlp2::amp2d_ff.
       *
       * To avoid accidental use of raw pointers, vlp2::amp2d_ff's
       * constructor is in a private implementation
       * class. vlp2::amp2d_ff::make is the public interface for
       * creating new instances.
       */
       static sptr make(float Ax, float Dz, float m, std::vector<float> CtCr, float A, float R, float Ts, float n, float fov, float tx_number);
      
      virtual void set_Ax(float Ax) = 0;
      virtual void set_Dz(float Dz) = 0;
      virtual void set_m(float m) = 0;
      virtual void set_CtCr(std::vector<float> CtCr, float A, float R, float Ts, float n, float fov) = 0;
      virtual void set_tx_number(float tx_number) = 0;
      virtual float Ax() = 0;
      virtual float Dz() = 0;
      virtual float m() = 0;
      virtual std::vector<float> CtCr() = 0;
      virtual float tx_number() = 0;
  
      
    };

  } // namespace vlp2
} // namespace gr

#endif /* INCLUDED_VLP2_AMP2D_FF_H */

