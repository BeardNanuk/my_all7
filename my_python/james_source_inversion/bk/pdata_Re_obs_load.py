#!/usr/bin/env python


## data recovered as numpy as, one is interpolated observed data; the other is received data generated from the inverted source time function 

## created on Tue Nov 13 20:43:18 STD 2018 
## created by Jiaze He

import pickle 

with open('obf/input/data_Re_obs.pickle','rb') as handle:
    #pipeline1 = pickle.load(handle)
    data_Re_obs = pickle.load(handle)

stream_syn = read('obf/input/Up_csic_f78_90_f04000000_DT4d_9.su',format='SU', byteorder='<')
data_Re_syn = _convert_to_array(stream_syn)


