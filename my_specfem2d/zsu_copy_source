#!/bin/bash

# generate a few signals for comparison between syn and obs

# revised on Tue Oct 16 20:14:21 UTC 2018
# created by Jiaze He


#flag_seismotype = 4
#flag_seismotype=`grep ^seismotype DATA/Par_file`
flag_seismotype=`grep ^seismotype DATA/Par_file | cut -d = -f 2 | cut -d \# -f 1 | tr -d ' '`
#f0=$(sed -n 1,15p DATA/SOURCE | grep 'f0' | cut -d\= -f2 | tr -d '[:space:]')
#echo 'f0 ='$f0
echo 'flag_seismotype ='$flag_seismotype
export flag_seismotype

D_T=`grep ^DT DATA/Par_file | cut -d = -f 2 | cut -d \# -f 1 | tr -d ' '| sed 's/-/\_/g'`
D_T=${D_T/d_/e-}
echo 'D_T ='$D_T

export D_T 

NSTEP=$(sed -n 26,28p DATA/Par_file | grep 'NSTEP' | cut -d\= -f2 | tr -d '[:space:]')
echo 'NSTEP ='$NSTEP
export NSTEP 


rm -f $HOME/specfem2d/obf/input/U*.su

cp ~/specfem2d/OUTPUT_FILES/U*.su $HOME/specfem2d/obf/input

python zobs_sig_comp
python zobs_sig_comp_p2

