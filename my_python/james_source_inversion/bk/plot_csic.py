#!/usr/bin/env python

#import obspy
#import numpy as np
#import pandas as pd
#from myFormat.data_format import para_struct
#from seisflows.tools.graphics import _convert_to_array
#from scipy.interpolate import interp1d
#
### for ploting
#import matplotlib.pyplot as plt 
#from seisflows.tools.graphics import plot_section
#
#import argparse
#
#
## for filtering
#from obspy.signal.filter import bandpass
#
#
##### for spectrum plotting
#from scipy import signal
##from obspy.signal.util import _npts2nfft
##from obspy.signal.invsim import cosine_sac_taper
#from scipy.fftpack import fft, ifft, fftfreq
#
##%matplotlib inline
#import matplotlib.pyplot as plt
#from obspy import read, UTCDateTime
### for i/o
##from obspy import read
#import scipy.io as sio 
#from obspy.core.stream import Stream
#import os  

#flag_obs_type = 2 # 1 for su, 2 for matlab 
#flag_plot_spectrum = 2 # 1 plot, 2 not plot
#
#if flag_obs_type is 1: 
#    stream_obs = read('obf/input/Up_gauss_f05000000.su',format='SU', byteorder='<')
#    data_obs = _convert_to_array(stream_obs)
#    
#elif flag_obs_type is 2:
#    from scipy.io import loadmat
#    matfile2=loadmat('obf/input/Fan01_SRC08_mat.mat')
#    data_obs = matfile2['fan_beam_scan_full']
#    #type(data_obs)
#print('the shape of the observed data: ', data_obs.shape)
#    
#
#stream_syn = read('obf/input/Up_gauss_f05000000.su',format='SU', byteorder='<')
#data_syn = _convert_to_array(stream_syn)
#print('the shape of the synthetic data: ', data_syn.shape)
#  
##trace_num = 150 
#
#trace_obs = data_obs[:,trace_num]
#print('shape of observed is :', trace_obs.shape)
#trace_syn = data_syn[:,trace_num]
#print('shape of synthetic signal is :', trace_syn.shape)
#
##### load stf function 
#stf_syn_pd = pd.read_csv('obf/input/stf_gaussian_f05000000',header=None,delim_whitespace=True)
#stf_syn_1Dnp = stf_syn_pd.values
#stf_syn = stf_syn_1Dnp[:,1]
#stf_obs_1Dnp = pd.read_csv('obf/input/stf_delayed_ricker_f0500000',header=None,delim_whitespace=True).values
#stf_obs = stf_obs_1Dnp[:,1]
#
#syn_name = 'gaussian'
#obs_name = 'tbd' # to be determined
#
#import h5py
#### load mat data over -v7.3
#with h5py.File('obf/input/Fan01_SRC08_para.mat', 'r') as file:
#    mystation_para = list(file['mystation']) # matrix filename is para 
#mystation_para

#plt.subplot(2, 1, 1)
#plt.plot(trace_obs[700:2700], 'k-')
#plt.title('quick peek')
#plt.ylabel('Damped oscillation')
#
#plt.subplot(2, 1, 2)
#plt.plot(trace_syn[4000:10000], 'r-')
#plt.xlabel('time (s)')
#plt.ylabel('Undamped')
#
#plt.tight_layout(rect=[0, 0, 2.5, 3])
#
#plt.show()

trace_obs = data_obs[:,trace_num]
print('shape of observed is :', trace_obs.shape)
trace_syn = data_syn[:,trace_num]
print('shape of synthetic signal is :', trace_syn.shape)

#### load stf function 
stf_syn_pd = pd.read_csv('obf/input/stf_gaussian_f05000000',header=None,delim_whitespace=True)
stf_syn_1Dnp = stf_syn_pd.values
stf_syn = stf_syn_1Dnp[:,1]
stf_obs_1Dnp = pd.read_csv('obf/input/stf_delayed_ricker_f0500000',header=None,delim_whitespace=True).values
stf_obs = stf_obs_1Dnp[:,1]

syn_name = 'gaussian'
obs_name = 'tbd' # to be determined

import h5py
### load mat data over -v7.3
with h5py.File('obf/input/Fan01_SRC08_para.mat', 'r') as file:
    mystation_para = list(file['mystation']) # matrix filename is para 
mystation_para



#####################
# create a class of structure that can be used to store parameters for 
from myFormat.data_format import para_struct
exp_para = para_struct('exp_para')
# load all parameters: 

f0=3500000; exp_para.f0 = f0
fmax = 10000000; exp_para.fmax = fmax
#output_time_step = 20000; exp_para.output_time_step = output_time_step;
dt = 6e-9; exp_para.dt = dt 
dtsyn = 6e-9; exp_para.dtsyn = dtsyn
dtobs = 5e-8; exp_para.dtobs = dtobs
#DownSampleFact=8; exp_para.DownSampleFact = DownSampleFact;
UpSampleFact = dtsyn/dtobs; 
UpSampleFact2 = 1; 
dtNew = dt*UpSampleFact; exp_para.dtNew = dtNew;
print('UpSampleFactor : %20.19f ' % UpSampleFact) 
#UpSampleFact2 = dtsyn 
## dt for after resampling 
dtNewobs = dtobs*UpSampleFact; exp_para.dtNewobs = dtNewobs;
dtNewsyn = dtsyn*UpSampleFact2; exp_para.dtNewsyn = dtNewsyn;
print('original sampling interval - syn: %20.19f s' % dtsyn)
print('original sampling interval - obs: %20.19f s' % dtobs)
print('sampling interval before resampling - dtNewsyn: %20.19f s' % dtNewsyn)
print('sampling interval before resampling - dtNewobs: %20.19f s' % dtNewobs)


##### sampling rate - original  
fssyn = 1.0/dtsyn; exp_para.fssyn=fssyn;
fsobs = 1.0/dtobs; exp_para.fsobs=fsobs;
print('sampling rate before resampling - syn: %f Hz' % fssyn)
print('sampling rate before resampling - obs: %f Hz' % fsobs)


#### sampling rate after resampling
fsNew=1./dtNew; exp_para.fsNew=fsNew;
fsNewsyn=1./dtNewsyn; exp_para.fsNewsyn=fsNewsyn;
fsNewobs=1./dtNewobs; exp_para.fsNewobs=fsNewobs;
print('sampling rate fsNewsyn after resampling - syn: %f Hz' % fsNewsyn)
print('sampling rate fsNewobs after resampling - obs: %f Hz' % fsNewobs)


#%%% about the filters 
half_width=400000; exp_para.half_width = half_width;
low_freq=100000; exp_para.low_freq = low_freq;
high_freq=900000; exp_para.high_freq = high_freq;
band=[low_freq,high_freq]; exp_para.band = band;
nyq_freq=2.5e7; exp_para.nyq_freq = nyq_freq;
####N=50000; exp_para.N = N;


#############

#SOURCE_SIGNAL_MATRIX=para.SOURCE_SIGNAL_MATRIX;

#%rawdata = para.rawdata;
Nt=28000; exp_para.Nt = Nt; 
#Na=20250; exp_para.Na = Na; 
NSrc=1; exp_para.NSrc = NSrc; 
NRec=176; exp_para.NRec = NRec;

Ntsyn=28000; exp_para.Ntsyn = Ntsyn;
Ntobs=3360; exp_para.Ntobs = Ntobs; 

## time steps after resamping
NtNewobs = int(Ntobs/UpSampleFact)
NtNewsyn = int(Ntsyn/UpSampleFact2)
print('time steps after resamping Ntnewobs = ',NtNewobs)

t_total = np.arange(dtNew,Nt*dtNew+dtNew,dtNew)
t_cut = t_total;exp_para.t_cut = t_cut

exp_para.t_total = t_total
t_total_syn = np.arange(dtsyn,Ntsyn*dtsyn+dtsyn,dtsyn)
exp_para.t_total_syn = t_total_syn
t_total_obs = np.arange(dtobs,Ntobs*dtobs+dtobs,dtobs)
exp_para.t_total_obs = t_total_obs

## time array - aftering resampling 
t_totalNew_obs = np.arange(dtNewobs,NtNewobs*dtNewobs+dtNewobs,dtNewobs)
exp_para.t_totalNew_obs = t_totalNew_obs

t_totalNew_syn = t_total_syn;
exp_para.t_totalNew_syn = t_totalNew_syn



sample_total = np.arange(1,Nt+1,1)
sample_syn = np.arange(1,Ntsyn+1,1)
sample_obs = np.arange(1,Ntobs+1,1)
#sample_cut = np.arange(1,output_time_step+1,1)
#sample_cut  = sample_total

### 1.0 filtering of the observed data 
import math as M
from future.utils import native
def next_pow_2(i):
    """
    Find the next power of two

    >>> int(next_pow_2(5))
    8
    >>> int(next_pow_2(250))
    256
    """
    # do not use NumPy here, math is much faster for single values
    buf = M.ceil(M.log(i) / M.log(2))
    return native(int(M.pow(2, buf)))

nfft = next_pow_2(Nt)
nfftsyn = next_pow_2(Ntsyn)
nfftobs = next_pow_2(Ntobs)

## length of total sampling points for fft, after resampling 
nfftNewobs = next_pow_2(NtNewobs)
nfftNewsyn = next_pow_2(NtNewsyn)
print('zero-padded length of fft nfftsyn - syn: %d ' % nfftsyn)
print('zero-padded length of fft nfftobs - obs: %d ' % nfftobs)

print('zero-padded length of fft nfftNewobs - obs: %d ' % nfftNewobs)
print('zero-padded length of fft nfftNewsyn - syn: %d ' % nfftNewsyn)
## df after padding
dfNew_pad = (fsNew/nfft)
dfNew_padsyn = (fsNewsyn/nfftsyn)
dfNew_padobs = (fsNewobs/nfftobs)
dfNew_padResyn = (fsNewsyn/nfftNewsyn)
dfNew_padReobs = (fsNewobs/nfftNewobs)

print('frequency intervel after zero-padding - syn: %f Hz' % dfNew_padsyn)
print('frequency intervel after zero-padding - obs: %f Hz' % dfNew_padobs)
print('frequency intervel after zero-padding - Newobs: %f Hz (actually used)' % dfNew_padReobs)
print('frequency intervel after zero-padding - Newsyn: %f Hz (actually used)' % dfNew_padResyn)


### 1.01 calculate the frequency spectrum for original signals before intepolations
xf = np.linspace(0.0, fsNew, nfft)

xf_obs = np.linspace(0.0, fsobs, nfftobs)
yf_obs = fft(trace_obs[0:Ntobs], axis=0, n=nfftobs)
print('shape of the original frequency range - obs:', xf_obs.shape)
print('shape of the original spectrum - obs:', yf_obs.shape)

### 1.03 resampling the signals such that sythetics and experimental data will match 
from scipy import interpolate

tck = interpolate.splrep(t_total_obs, trace_obs, s=0)
traceNew_obs = interpolate.splev(t_totalNew_obs, tck, der=0)
traceNew_syn = trace_syn;
print('shape of the interpolated signal - traceNew_obs.shape:', traceNew_obs.shape)
print('shape of the interpolated signal - traceNew_syn.shape:', traceNew_syn.shape)

xf_Newobs = np.linspace(0.0, fsNewobs, nfftNewobs)
xf_Newsyn = np.linspace(0.0, fsNewsyn, nfftNewsyn)
yf_Newobs = fft(traceNew_obs, axis=0, n=nfftNewobs)
yf_Newsyn = fft(traceNew_syn, axis=0, n=nfftNewsyn)
print('shape of the interpolated frequency range - xf_Newobs.shape:', xf_Newobs.shape)
print('shape of the interpolated spectrum - yf_Newobs.shape:', yf_Newobs.shape)
print('shape of the interpolated frequency range - xf_Newsyn.shape:', xf_Newsyn.shape)
print('shape of the interpolated spectrum - yf_Newsyn.shape:', yf_Newsyn.shape)


### 1.04 filtering the resampled signal 
freqmin=100000
freqmax=5000000

# filtering
#stf_filtered = bandpass(stf_cut_nodelay, freqmin, freqmax, fs_new, zerophase=True)
#traceNew_obs_filtered = bandpass(traceNew_obs, freqmin, freqmax, fsNewobs, zerophase=True)
#traceNew_filtered = fft(traceNew_obs_filtered, axis=0, n=nfftNewobs)

traceNew_detrendobs = np.copy(signal.detrend(traceNew_obs))
yf_traceNew_detrendobs = fft(traceNew_detrendobs, axis=0, n=nfftNewobs)
traceNew_detrend_filteredobs = bandpass(traceNew_detrendobs, freqmin, freqmax, fsNewobs, zerophase=True)
yf_traceNew_detrend_filteredobs = fft(traceNew_detrend_filteredobs, axis=0, n=nfftNewobs)

#stf_cut_nodelay_detrend_filtered = bandpass(stf_cut_nodelay_detrend, freqmin, freqmax, fs_new, zerophase=True)
#yf_detrend_filtered = fft(stf_cut_nodelay_detrend_filtered, axis=0, n=nfft) 

### 1.05 plot FFT results for resampling
freq_show_star = 100000
freq_show_end = 9000000

freq_step_star = int(round(freq_show_star/dfNew_pad))
print(freq_step_star)
freq_step_end = int(round(freq_show_end/dfNew_pad))
print(freq_step_end)

freq_step_starNewobs = int(round(freq_show_star/dfNew_padReobs))
print('freq_step_starNewobs',freq_step_starNewobs)
freq_step_endNewobs = int(round(freq_show_end/dfNew_padReobs))
print('freq_step_endNewobs',freq_step_endNewobs)

freq_step_starNewsyn = int(round(freq_show_star/dfNew_padResyn))
print('freq_step_starNewsyn',freq_step_starNewsyn)
freq_step_endNewsyn = int(round(freq_show_end/dfNew_padResyn))
print('freq_step_endNewsyn',freq_step_endNewsyn)


# plot the received signals
time_star= 1200 * dtobs
time_end = 2700 * dtobs


t_star_show = int(time_star/dtNew)
t_end_show = int(time_end/dtNew)

t_star_showsyn = int(time_star/dtsyn)
t_end_showsyn = int(time_end/dtsyn)

t_star_showobs = int(time_star/dtobs)
t_end_showobs = int(time_end/dtobs)

t_starNew_showobs = int(time_star/dtNewobs)
t_endNew_showobs = int(time_end/dtNewobs)

if flag_plot_spectrum is 1:

   fig, (ax0,ax1,ax2,ax3,ax4,ax5) = plt.subplots(nrows=6)
   
   ax0.plot(xf_obs/1000,np.abs(yf_obs),'-k')
   ax0.set_title('observed - ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax0.set_xlabel('frequency (kHz)')
   
   ax1.plot(xf_Newobs/1000,np.abs(yf_Newobs),'-k')
   ax1.set_title('observed w resampling - ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax1.set_xlabel('frequency (kHz)')
   
   ax2.plot(t_total_obs[t_star_showobs:t_end_showobs],trace_obs[t_star_showobs:t_end_showobs],'k-')
   ax2.set_title('observed - ' + str(obs_name) + ' trace ' + str(trace_num))
   ax2.set_xlabel('time (us)')


   ax3.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_Newobs[freq_step_starNewobs:freq_step_endNewobs]),'-k')
   ax3.set_title('observed w resampling - zoom-in ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax3.set_xlabel('frequency (kHz)')
  
   ax4.plot(t_total_syn[t_star_showsyn:t_end_showsyn],trace_syn[t_star_showsyn:t_end_showsyn],'b-')
   ax4.set_title('synthetic - ' + str(syn_name) + ' trace ' + str(trace_num))
   ax4.set_xlabel('time (us)')
 
   #ax3.plot(xf_Newobs[freq_step_starNew:freq_step_endNew]/1000,np.abs(yf_traceNew_detrendobs[freq_step_starNew:freq_step_endNew]),'-b')
   #ax3.set_title('observed w resampling detrend - zoom-in ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   #ax3.set_xlabel('frequency (kHz)')
   
   #ax4.plot(xf_Newobs[freq_step_starNew:freq_step_endNew]/1000,np.abs(yf_traceNew_detrend_filteredobs[freq_step_starNew:freq_step_endNew]),'-k')
   #ax4.set_title('observed w resampling detrend filtered - zoom-in ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   #ax4.set_xlabel('frequency (kHz)')
   
   ax5.plot(xf_Newsyn[freq_step_starNewsyn:freq_step_endNewsyn]/1000,np.abs(yf_Newsyn[freq_step_starNewsyn:freq_step_endNewsyn]),'-b')
   ax5.set_title('synthetics w resampling - zoom-in ' + str(syn_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax5.set_xlabel('frequency (kHz)')


   
   plt.tight_layout(rect=[0, 0, 1.5, 2])
   u_receives_signals_fn = 'obf/output/csic/src01_rec%02d_spectrum.png' % (trace_num)
   plt.savefig(u_receives_signals_fn,format='png', dpi=200, bbox_inches='tight')
   fig.show()
   #plt.close()
