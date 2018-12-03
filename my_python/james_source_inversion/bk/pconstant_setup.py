#!/usr/bin/env python

### constant generation

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He

## revised on Tue Nov 13 20:43:18 STD 2018
## add the trace range: inv_trace_num_star inv_trace_num_end

#inv_trace_num_star = 88 
#inv_trace_num_end = 89 

#####################
# create a class of structure that can be used to store parameters for 
from myFormat.data_format import para_struct
exp_para = para_struct('exp_para')
# load all parameters: 

flag_plot_spectrum = 1 # 1 plot, 2 not plot
flag_check_recovered = 2 # 1 run 2 not run 
flag_stf_inverse = 1 # 1 run 2 not run 
flag_plot_inverted_stf = 1 # 1 plot # 2 not plot
flag_save_inverted_stf = 1 # 1 save # 2 not save 



syn_name = 'gaussian'
obs_name = 'tbd' # to be determined



f0=3500000; exp_para.f0 = f0
fmax = 10000000; exp_para.fmax = fmax
#output_time_step = 20000; exp_para.output_time_step = output_time_step;
dt = 4e-9; exp_para.dt = dt 
dtsyn = 4e-9; exp_para.dtsyn = dtsyn
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
Nt=42000; exp_para.Nt = Nt; 
#Na=20250; exp_para.Na = Na; 
NSrc=1; exp_para.NSrc = NSrc; 
NRec=176; exp_para.NRec = NRec;

Ntsyn=42000; exp_para.Ntsyn = Ntsyn;
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
#yf_obs = fft(trace_obs[0:Ntobs], axis=0, n=nfftobs)
print('shape of the original frequency range - obs:', xf_obs.shape)
#print('shape of the original spectrum - obs:', yf_obs.shape)

#### 1.03 resampling the signals such that sythetics and experimental data will match 
#from scipy import interpolate
#
#tck = interpolate.splrep(t_total_obs, trace_obs, s=0)
#traceNew_obs = interpolate.splev(t_totalNew_obs, tck, der=0)
#traceNew_syn = trace_syn;
#print('shape of the interpolated signal - traceNew_obs.shape:', traceNew_obs.shape)
#print('shape of the interpolated signal - traceNew_syn.shape:', traceNew_syn.shape)
#
#xf_Newobs = np.linspace(0.0, fsNewobs, nfftNewobs)
#xf_Newsyn = np.linspace(0.0, fsNewsyn, nfftNewsyn)
#yf_Newobs = fft(traceNew_obs, axis=0, n=nfftNewobs)
#yf_Newsyn = fft(traceNew_syn, axis=0, n=nfftNewsyn)
#print('shape of the interpolated frequency range - xf_Newobs.shape:', xf_Newobs.shape)
#print('shape of the interpolated spectrum - yf_Newobs.shape:', yf_Newobs.shape)
#print('shape of the interpolated frequency range - xf_Newsyn.shape:', xf_Newsyn.shape)
#print('shape of the interpolated spectrum - yf_Newsyn.shape:', yf_Newsyn.shape)


### 1.03 resampling the signals such that sythetics and experimental data will match 
xf_Newobs = np.linspace(0.0, fsNewobs, nfftNewobs)
xf_Newsyn = np.linspace(0.0, fsNewsyn, nfftNewsyn)
print('shape of the interpolated frequency range - xf_Newobs.shape:', xf_Newobs.shape)
#print('shape of the interpolated spectrum - yf_Newobs.shape:', yf_Newobs.shape)
print('shape of the interpolated frequency range - xf_Newsyn.shape:', xf_Newsyn.shape)
#print('shape of the interpolated spectrum - yf_Newsyn.shape:', yf_Newsyn.shape)


### 1.04 filtering the resampled signal 
freqmin=100000
freqmax=5000000

# filtering
#stf_filtered = bandpass(stf_cut_nodelay, freqmin, freqmax, fs_new, zerophase=True)
#traceNew_obs_filtered = bandpass(traceNew_obs, freqmin, freqmax, fsNewobs, zerophase=True)
#traceNew_filtered = fft(traceNew_obs_filtered, axis=0, n=nfftNewobs)

####traceNew_detrendobs = np.copy(signal.detrend(traceNew_obs))
####yf_traceNew_detrendobs = fft(traceNew_detrendobs, axis=0, n=nfftNewobs)
####traceNew_detrend_filteredobs = bandpass(traceNew_detrendobs, freqmin, freqmax, fsNewobs, zerophase=True)
####yf_traceNew_detrend_filteredobs = fft(traceNew_detrend_filteredobs, axis=0, n=nfftNewobs)

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
time_star= 1100 * dtobs
time_end = 1500 * dtobs


t_star_show = int(time_star/dtNew)
t_end_show = int(time_end/dtNew)

t_star_showsyn = int(time_star/dtsyn)
t_end_showsyn = int(time_end/dtsyn)

t_star_showobs = int(time_star/dtobs)
t_end_showobs = int(time_end/dtobs)

t_starNew_showobs = int(time_star/dtNewobs)
t_endNew_showobs = int(time_end/dtNewobs)

#execfile('pplot_one_spectrum.py')

