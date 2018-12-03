#!/usr/bin/env python

### signal comparison: individual trace preprocessing, loading and fft

## created on Thu Nov 15 22:47:15 STD 2018
## created by Jiaze He 


trace_interp_obs = data_Re_obs[:NtsynNew:10,trace_num]
#print('shape of observed is :', trace_interp_obs.shape)
trace_Re_syn = - data_Re_syn[:Ntcomp,trace_num]
#print('shape of inverted source signal is :', trace_Re_syn.shape)

#yf_Newobs_ = fft(trace_obs, axis=0, n=nfftNewobs)
# fft of the newly recovered signals
yf_trace_interp_obs = fft(trace_interp_obs, axis=0, n=nfftNewobs)
yf_trace_inverted_syn = fft(trace_Re_syn, axis=0, n=nfftNewsyn)


#execfile('pplot_Re_one_spectrum.py')


