#!/usr/bin/env python


## filtering the inverted stf signal

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 

## revised on Fri Nov  9 16:49:50 UTC 2018
##

stf_inverted_trace_filtered = bandpass(stf_inverted, freqmin, freqmax, fsNewobs, zerophase=True)
yf_stf_inverted_trace_filtered = fft(stf_inverted_trace_filtered, axis=0, n=nfftNewsyn)



