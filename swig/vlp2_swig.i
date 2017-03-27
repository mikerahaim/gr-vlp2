/* -*- c++ -*- */

#define VLP2_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "vlp2_swig_doc.i"

%{
#include "vlp2/amp2d_fixed_height.h"
#include "vlp2/amp2d_ff.h"
#include "vlp2/trilat_scaleable_ff.h"
%}


%include "vlp2/amp2d_fixed_height.h"
GR_SWIG_BLOCK_MAGIC2(vlp2, amp2d_fixed_height);
%include "vlp2/amp2d_ff.h"
GR_SWIG_BLOCK_MAGIC2(vlp2, amp2d_ff);


%include "vlp2/trilat_scaleable_ff.h"
GR_SWIG_BLOCK_MAGIC2(vlp2, trilat_scaleable_ff);
