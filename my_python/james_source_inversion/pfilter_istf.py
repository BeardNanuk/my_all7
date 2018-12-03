#!/usr/bin/env python

## filtering the inverted stf signal

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 

## revised on Fri Nov  9 16:49:50 UTC 2018
##
##if (flag_istf_using_stack is 1):
stf_inverted_stack_trace_filtered = bandpass(stf_inverted_stack, freqmin, freqmax, fsNewobs, zerophase=True)
yf_stf_inverted_stacked_trace_filtered = fft(stf_inverted_stack_trace_filtered, axis=0, n=nfftNewsyn)
##elif (flag_istf_using_stack is 2):
stf_inverted_trace_filtered = bandpass(stf_inverted, freqmin, freqmax, fsNewobs, zerophase=True)
yf_stf_inverted_trace_filtered = fft(stf_inverted_trace_filtered, axis=0, n=nfftNewsyn)

### experimental data
traceNew_obs_filtered = bandpass(traceNew_obs, freqmin, freqmax, fsNewobs, zerophase=True)
yf_traceNew_obs_filtered = fft(traceNew_obs_filtered, axis=0, n=nfftNewsyn)

#stf_inverted_stack_trace_filtered = bandpass(stf_inverted_stack, freqmin, freqmax, fsNewobs, zerophase=True)
#yf_stf_inverted_stacked_trace_filtered = fft(stf_inverted_stack_trace_filtered, axis=0, n=nfftNewsyn)

