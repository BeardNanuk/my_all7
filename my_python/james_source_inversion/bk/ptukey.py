#!/usr/bin/env python


#We now generate the frequency filter that has already been applied to the processed field data. We plot the filter to verify.

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He

## revised on Tue Nov 13 20:43:18 STD 2018
## alpha from 0.01 to 0.05


import numpy as np
from scipy import signal
from obspy.signal.util import _npts2nfft
from scipy.fftpack import fft, ifft, fftfreq

# Setup prefilter with cosine taper
#npts = len(field_trace.data) # resampled trace so different from FieldDataProcessing
#print('npts',npts)
#nfft = _npts2nfft(npts)

tukey_end_freq = 8000000
tukey_length = int(round(tukey_end_freq/dfNew_padResyn))
print('tukey_length',tukey_length)

print('nfft',nfft)
print('nfftNewobs',nfftNewobs)

#freq_pos = signal.tukey(tukey_length, alpha=0.01)
freq_pos = signal.tukey(tukey_length, alpha=0.001)
print('freq_pos.shape - tukey',freq_pos.shape)
freq_pos = np.pad(freq_pos, 1,'constant',constant_values=0)
print('freq_pos.shape - pad',freq_pos.shape)
freq_pos.resize(nfftNewobs/2)
print('freq_pos.shape - resize',freq_pos.shape)
freq_neg = freq_pos[::-1]
print('freq_neg.shape - freq_pos[::-1]',freq_neg.shape)
syn_taper = np.append(freq_pos, freq_neg)
print('syn_taper.shape - append',syn_taper.shape)
syn_taper
# Plot the filter
freqs = fftfreq(nfftNewsyn, d=dfNew_padResyn)
#freqs = fftfreq(nfft, d=0.000000003)




#plt.plot(freqs[0:120]/1e3,freq_pos[0:120])
plt.plot(xf_Newobs[freq_step_starNewsyn-1:freq_step_endNewsyn-1]/1e3,freq_pos[freq_step_starNewsyn-1:freq_step_endNewsyn-1])
plt.title('Tukey Window Taper Applied')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Gain')
plt.show()
