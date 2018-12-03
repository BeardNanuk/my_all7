#!/usr/bin/env python

# python version of - from matlab txt filter to source file for specfem2d (also txt)

# revised on Tue Oct 16 20:14:21 UTC 2018
# created by Jiaze He


# official library loading
import scipy.io as sio

## Simple demo with multiple subplots.
import numpy as np
import matplotlib.pyplot as plt
#import h5py

# for filtering
from obspy.signal.filter import bandpass

#### for spectrum plotting
from scipy import signal
#from obspy.signal.util import _npts2nfft
#from obspy.signal.invsim import cosine_sac_taper
from scipy.fftpack import fft, ifft, fftfreq 


# create a class of structure that can be used to store parameters for 
from myFormat.data_format import para_struct
exp_para = para_struct('exp_para')

# load all parameters: 

f0=500000; exp_para.f0 = f0
fmax = 1000000; exp_para.fmax = fmax
output_time_step = 20000; exp_para.output_time_step = output_time_step; 
dt = 2.5e-9; exp_para.dt = dt
DownSampleFact=8; exp_para.DownSampleFact = DownSampleFact;
dtNew = 2.0e-8; exp_para.dtNew = dtNew;
#fs = 5e7;
#time = para.time;
#timestep_star =para.timestep_star; timestep_end = para.timestep_end;
###time_my = para.time_my(1,1:output_time_step);
#rawdata2= para.rawdata2;
#%source function 
#source_time_filtered_function_temp= para.rawdata2(:,225);

#%%% about the filters 
half_width=400000; exp_para.half_width = half_width;
low_freq=100000; exp_para.low_freq = low_freq;
high_freq=900000; exp_para.high_freq = high_freq;
band=[low_freq,high_freq]; exp_para.band = band;
nyq_freq=2.5e7; exp_para.nyq_freq = nyq_freq;
#band_norm=
#order=para.order;fir_coeff=para.fir_coeff; 

N=50000; exp_para.N = N;
#filtered_signal=para.filtered_signal;
#filtered_signal_spec=para.filtered_signal_spec;
#absfiltered_signal_spec=para.absfiltered_signal_spec;
#delay_step_for_exp=para.delay_step_for_exp;
#source_time_filtered_function_original= para.source_time_filtered_function_original;
#%%% 

#SOURCE_SIGNAL_MATRIX=para.SOURCE_SIGNAL_MATRIX;

##%%% 
#%rawdata = para.rawdata;
Nt=50000; exp_para.Nt = Nt;
Na=20250; exp_para.Na = Na;
NSrc=45; exp_para.NSrc = NSrc; 
NRec=450; exp_para.NRec = NRec;


# load the received signal from the transducer

t_total = np.arange(dtNew,Nt*dtNew+dtNew,dtNew)
exp_para.t_total = t_total
t_cut = np.arange(dtNew,output_time_step*dtNew+dtNew,dtNew)
exp_para.t_cut = t_cut
sample_total = np.arange(1,Nt+1,1)
sample_cut = np.arange(1,output_time_step+1,1)
# load the unfiltered signal from the transducer
stf_unfiltered_original = np.loadtxt("obf/input/unfiltered_signal_no_delay")
#source_time_filtered_function_original = np.loadtxt("unfiltered_signal_no_delay")

import pickle
pickle.dump(exp_para,open('obf/input/exp_para.pickle','wb'))

print('parameter recreation is done')

### 1.1 Input signal plot
# plot the received signal (total and zoom-in)
t_star_show = 13014
t_end_show = 16014


###fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
###
###ax0.plot(t_total,stf_unfiltered_original,'b-')
###ax0.set_title('total unfiltered, directly recevied signals')
###ax0.set_ylabel('received signals')
###
####ax1.subplot(2, 1, 1)
###ax1.plot(t_cut[t_star_show:t_end_show],stf_unfiltered_original[t_star_show:t_end_show],'-')
###ax1.set_title('zoom-in unfiltered, directly recevied signals')
###ax1.set_ylabel('received signals')
###
####ax1.subplot(2, 1, 1)
###ax2.plot(sample_total[t_star_show:t_end_show],stf_unfiltered_original[t_star_show:t_end_show],'-')
###ax2.set_title('zoom-in unfiltered, sample')
###ax2.set_ylabel('received signals')

#plt.tight_layout(rect=[0, 0, 2.4, 0.9])

#plt.show()





### 1.2 cut out the main peaks as the direct arrival

#source_time_cut_function_temp = np.copy(stf_unfiltered_original)
stf_cut_temp = np.copy(stf_unfiltered_original)
timestep_star = 13500
timestep_end = 14250

stf_cut_temp[timestep_star:timestep_end] = 0
stf_cut = stf_unfiltered_original - stf_cut_temp

#### plot the received signal (total and zoom-in)
###fig, (ax0,ax1) = plt.subplots(nrows=2)
####ax0.subplot(2, 1, 2)
###ax0.plot(sample_total,stf_cut,'b-')
###ax0.set_title('total cut signals')
####ax0.set_ylabel('received signals')
###
###ax1.plot(sample_total[t_star_show:t_end_show],stf_cut[t_star_show:t_end_show],'-')
###ax1.set_title('zoom-in unfiltered, sample')
#ax1.set_ylabel('received signals')

#plt.tight_layout(rect=[0, 0, 1.5, 1])

print('get the main peaks')
#plt.show()

### 1.3 apply the intial guessed delay 

#stf_cut_nodelay = np.zeros((output_time_step,1))
stf_cut_nodelay = np.copy(stf_unfiltered_original[0:output_time_step]/(stf_unfiltered_original.max().max()))
#stf_cut_nodelay= np.copy(stf_unfiltered_original)
stf_cut_nodelay[:]= 0


#source_time_cut_function_no_delay = np.zeros((output_time_step,1))
delay_step_for_exp = 13614 + 45 
stf_cut_nodelay[0:output_time_step-delay_step_for_exp]= np.copy(stf_cut[delay_step_for_exp:output_time_step])

# plot the received signal (total and zoom-in)
###fig, (ax0,ax1,ax2,ax3) = plt.subplots(nrows=4)
###
###ax0.plot(sample_total[t_star_show:t_end_show],stf_cut[t_star_show:t_end_show],'-')
###ax0.set_title('source_time_cut_function,zoom-in')
###ax0.set_xlabel('sampling points')
###
####ax0.subplot(2, 1, 2)
###ax1.plot(sample_cut,stf_cut[0:output_time_step],'b-')
###ax1.set_title('source_time_cut_function  ')
###ax1.set_xlabel('sampling points')
####ax0.set_ylabel('received signals')
###
####ax0.subplot(2, 1, 2)
###ax2.plot(sample_total[(t_star_show-delay_step_for_exp):(t_end_show-delay_step_for_exp)],stf_cut_nodelay[(t_star_show-delay_step_for_exp):(t_end_show-delay_step_for_exp)],'-')
###ax2.set_title('initial delay removed - zoom-in')
###ax2.set_xlabel('sampling points')
####ax0.set_ylabel('received signals')
###
####ax0.subplot(2, 1, 2)
###ax3.plot(sample_cut,stf_cut_nodelay,'b-')
###ax3.set_title('initial delay removed ')
###ax3.set_xlabel('sampling points')
####ax0.set_ylabel('received signals')
###
####plt.tight_layout(rect=[0, 0, 1.5, 2])
####fig.show()
######plt.show()


### 1.4 zero padding for reliable FFT

from myFormat.dsp import next_pow_2 
#import math as M
#from future.utils import native
#def next_pow_2(i):
#    """
#    Find the next power of two
#
#    >>> int(next_pow_2(5))
#    8
#    >>> int(next_pow_2(250))
#    256
#    """
#    # do not use NumPy here, math is much faster for single values
#    buf = M.ceil(M.log(i) / M.log(2))
#    return native(int(M.pow(2, buf)))

# signal filtering


fs=1./dt
print('original sampling frequency in experimental data (not used): %f Hz' % fs)
fs_new=1./dtNew
print('new sampling frequency after resampling: %f Hz' % fs_new)

nfft = next_pow_2(output_time_step)
print('zero-padded length of fft: %d ' % nfft)

#df_new = int(round(fs_new/nfft))
#print(df_new_round)
df_new = (fs_new/output_time_step)
df_new_pad = (fs_new/nfft)

print('frequency intervel before zero-padding: %f Hz ' % df_new)
print('frequency intervel after zero-padding: %f Hz (actually used)' % df_new_pad)



### 1.5 calculate the frequency spectrum for sft with cut/delay_removal

freq_show_star = 6000
freq_show_end = 1500000

freq_step_star = int(round(freq_show_star/df_new))
print(freq_step_star)
freq_step_end = int(round(freq_show_end/df_new))
print(freq_step_end)

xf = np.linspace(0.0, fs_new, nfft)
yf_original_same_length = fft(stf_unfiltered_original[0:output_time_step], axis=0, n=nfft)
yf = fft(stf_cut_nodelay, axis=0, n=nfft) 

### 1.6 plot FFT results of source_time_cut_function_no_delay
# sff - source frequency function 
###fig, (ax0,ax1,ax2,ax3) = plt.subplots(nrows=4)
###
####ax0.subplot(2, 1, 2)
###ax0.plot(xf/1000,yf,'-r')
###ax0.set_title('sff delay removed - real part (not useful)')
###ax0.set_xlabel('frequency (kHz)')
####ax0.set_ylabel('received signals')
###
###ax1.plot(xf/1000,np.abs(yf),'-r')
###ax1.set_title('sff delay removed  - absolute_value - first half')
###ax1.set_xlabel('frequency (kHz)')
###
#### ax1.plot(xf[0:output_time_step//2]/1000,np.abs(yf[0:output_time_step//2]),'-r')
#### ax1.set_title('sff delay removed  - absolute_value - first half')
#### ax1.set_xlabel('frequency (kHz)')
###
###ax2.plot(xf[freq_step_star-1:freq_step_end-1]/1000,np.abs(yf[freq_step_star-1:freq_step_end-1]),'-r')
###ax2.set_title('sff delay removed - absolute_value - zoom in')
###ax2.set_xlabel('frequency (kHz)')
###
###
#### ax3.plot(xf[freq_step_star-1:freq_step_end-1]/1000,np.abs(yf_original_same_length[freq_step_star-1:freq_step_end-1]),'b-')
#### ax3.set_title('original spectrum - same time length ')
#### ax3.set_xlabel('frequency (kHz)')
###
###ax3.plot(xf/1000,np.abs(yf_original_same_length),'b-')
###ax3.set_title('original spectrum - same time length ')
###ax3.set_xlabel('frequency (kHz)')


#plt.tight_layout(rect=[0, 0, 1.5, 2])

###plt.show()

### 1.7 Try the bandpass function in obspy



freqmin=50000
freqmax=950000

print(fs_new)

# filtering
#stf_filtered = bandpass(stf_cut_nodelay, freqmin, freqmax, fs_new, zerophase=True)
stf_filtered = bandpass(stf_cut_nodelay, freqmin, freqmax, fs_new, zerophase=True)
yf_filtered = fft(stf_filtered, axis=0, n=nfft)

stf_cut_nodelay_detrend = np.copy(signal.detrend(stf_cut_nodelay))
yf_detrend = fft(stf_cut_nodelay_detrend, axis=0, n=nfft)
stf_cut_nodelay_detrend_filtered = bandpass(stf_cut_nodelay_detrend, freqmin, freqmax, fs_new, zerophase=True)
yf_detrend_filtered = fft(stf_cut_nodelay_detrend_filtered, axis=0, n=nfft) 


# plot the received signal (total and zoom-in)
fig, (ax0,ax1,ax2,ax3) = plt.subplots(nrows=4)


#ax0.subplot(2, 1, 2)
#ax0.plot(sample_total[(t_star_show-delay_step_for_exp):(t_end_show-delay_step_for_exp)],stf_cut_nodelay[(t_star_show-delay_step_for_exp):(t_end_show-delay_step_for_exp)],'-')
#ax0.set_title('stf no delay')
#ax0.set_xlabel('sampling points')

ax0.plot(sample_total,stf_unfiltered_original,'b-')
ax0.set_title('total original signal')

ax1.plot(xf/1000,np.abs(yf_original_same_length),'b-')
ax1.set_title('original spectrum - same time length ')
ax1.set_xlabel('frequency (kHz)')

#ax1.plot(xf[freq_step_star-1:freq_step_end-1]/1000,np.abs(yf[freq_step_star-1:freq_step_end-1]),'-r')
#ax1.set_title('sff no delay - absolute_value')
#ax1.set_xlabel('frequency (kHz)')
#
##ax2.plot(sample_total[(t_star_show-delay_step_for_exp):(t_end_show-delay_step_for_exp)],stf_filtered[(t_star_show-delay_step_for_exp):(t_end_show-delay_step_for_exp)],'-')
##ax2.set_title('stf filtering w/o detrend')
##ax2.set_xlabel('sampling points')
##
##ax3.plot(xf[freq_step_star-1:freq_step_end-1]/1000,np.abs(yf_filtered[freq_step_star-1:freq_step_end-1]),'-r')
##ax3.set_title('sff filtering w/o detrend')
##ax3.set_xlabel('frequency (kHz)')
##
##ax4.plot(sample_total[(t_star_show-delay_step_for_exp):(t_end_show-delay_step_for_exp)],stf_cut_nodelay_detrend[(t_star_show-delay_step_for_exp):(t_end_show-delay_step_for_exp)],'-')
##ax4.set_title('stf cut/delay_removal/detrended ')
##ax4.set_xlabel('frequency (kHz)')
##
##ax5.plot(xf[freq_step_star-1:freq_step_end-1]/1000,np.abs(yf_detrend[freq_step_star-1:freq_step_end-1]),'-r')
##ax5.set_title('sff cut/delay_removal/detrended')
##ax5.set_xlabel('frequency (kHz)')

ax2.plot(sample_total[0:1000],stf_cut_nodelay_detrend_filtered[0:1000],'-')
ax2.set_title('stf cut/delay_removal/detrended/filtered ')
ax2.set_xlabel('frequency (kHz)')

ax3.plot(xf[freq_step_star-1:freq_step_end-1]/1000,np.abs(yf_detrend_filtered[freq_step_star-1:freq_step_end-1]),'-r')
ax3.set_title('sff filtered then detrended/filtered')
ax3.set_xlabel('frequency (kHz)')

fig.tight_layout()
#plt.tight_layout(rect=[0, 0, 1.5, 2.0])
#
plt.show()
#plt.show()
fig.savefig('obf/output/Un.png', format='png', dpi=1000)

### 1.8 save the signal as specfem's input

stf = open("obf/output/stf_cut_3rd_filtered_20000","w")

for i in range(0,output_time_step):#nstep + delay):
    stf.write("%20.19f " %t_cut[i])
    stf.write("%20.19f\n" %stf_cut_nodelay_detrend_filtered[i] )
    # to make sure the i/o is correct with the write function 
    print(i)














