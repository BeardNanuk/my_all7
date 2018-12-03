#!/usr/bin/env python

### individual trace preprocessing, loading and fft

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 


trace_obs = data_obs[:,trace_num]
#print('shape of observed is :', trace_obs.shape)
trace_syn = data_syn[:,trace_num]
#print('shape of synthetic signal is :', trace_syn.shape)

yf_obs = fft(trace_obs, axis=0, n=nfftobs)

### 1.03 resampling the signals such that sythetics and experimental data will match 

tck = interpolate.splrep(t_total_obs, trace_obs, s=0)
traceNew_obs = interpolate.splev(t_totalNew_obs, tck, der=0)
traceNew_syn = trace_syn;
#print('shape of the interpolated signal - traceNew_obs.shape:', traceNew_obs.shape)
#print('shape of the interpolated signal - traceNew_syn.shape:', traceNew_syn.shape)

yf_Newobs = fft(traceNew_obs, axis=0, n=nfftNewobs)
yf_Newsyn = fft(traceNew_syn, axis=0, n=nfftNewsyn)




