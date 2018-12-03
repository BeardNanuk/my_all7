#!/usr/bin/env python

import time
import math
import sys
import numpy as np
from seisflows.plugins import adjoint, misfit, readers, writers
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
from obspy.core import Stream, Trace
from obspy.signal.filter import bandpass
from scipy.signal import resample


freqmin=1
freqmax=50000

dt=0.00000008
df=(1./dt)

resamp = 0
nstep_resamp = 400

# 0 : Read the stf from a file
file = 'OUTPUT_FILES/plot_source_time_function.txt'
f=open(file,"r")
lines=f.readlines()
stf=[]
nstep=0
for x in lines:
    stf.append(float(x.split()[1]))
    #if (nstep<300):
    #  print x
    #  print stf[nstep]
    nstep=nstep+1
f.close()

plt.plot(stf)

print 'Number of timesteps : ' + str(nstep)

# 1 : Guess the delay to apply to the stf such that the filtered stf starts with a value close to 0 
filt_stf = bandpass(stf, freqmin, freqmax, df, zerophase=True)
tol = max(abs(filt_stf))/1000
i_max = np.argmax(abs(filt_stf))
ind = nstep - 1 
while (filt_stf[ind] < tol ):
  ind -=1

delay = ind - i_max
print 'Delay used : ' + str(delay)

#delay=16

# 2 : Apply delay and bandpass source time function
delayed_stf = np.zeros(nstep + delay )
delayed_stf[-nstep:] = np.array(stf)

resu = bandpass(delayed_stf, freqmin, freqmax, df, zerophase=True)
#t=Trace()
#t.data=resu
#t.taper(0.005, type='hann')
#resu = t.data

#if resamp ==1 :
#   resu = resample(resu[:nstep],int(1.5*nstep_resamp))[:nstep_resamp]

plt.figure(1)
#plt.plot(resu)
#plt.figure(1)
#plt.plot(result)
plt.plot(delayed_stf)
plt.show()
stf = open("my_filtered_stf.txt","w")

for i in range(0,nstep):#nstep + delay):
   stf.write("%d " %i)
   stf.write("%f\n"  %delayed_stf[i] )

