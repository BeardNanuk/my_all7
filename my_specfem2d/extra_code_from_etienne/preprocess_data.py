import time
import math
import sys
import numpy as np
from seisflows.plugins import adjoint, misfit, readers, writers
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
from obspy.core import Stream, Trace
# define seismic data reader and writer
reader = getattr(readers,'su')
writer = getattr(writers, 'su')

#output = Stream()

obs = reader('specfem2d/data/','obs.su')
obs_empty = reader('specfem2d/data/','obs_empty.su')
syn_empty = reader('specfem2d/data/','syn_empty.su')
l = len(obs[1].data)
#print len(obs)
#mask = np.sin(np.linspace(0.,math.pi,len(obs[1].data), dtype=np.float32))
#mask = np.zeros(len(obs[1].data),dtype=np.float32)
#mask[800:len(obs[1].data)] = np.sin(np.linspace(0.,math.pi,len(obs[1].data)-800, dtype=np.float32))
p=0.04
data1  = reader('specfem2d/data_reference/000000/','syn.su')
data1[50].taper(max_percentage=p,type='hann')
target = data1[50].data
print data1[50].stats

output = obs
for i in range(0,len(obs)):

   obs[i].detrend('demean')
   obs_empty[i].detrend('demean')
   syn_empty[i].detrend('demean')

   obs[i].taper(max_percentage=p,type='hann')
   obs_empty[i].taper(max_percentage=p,type='hann')
   syn_empty[i].taper(max_percentage=p,type='hann')


   obs_tr = obs[i].data
   obs_empty_tr = obs_empty[i].data
   syn_empty_tr = syn_empty[i].data
   t1 = obs_tr
   t2 = obs_empty_tr
   t3 = syn_empty_tr

   t1 = np.zeros(int(round(len(obs_tr)+3)),dtype=np.float32)
   t2 = np.zeros(int(round(len(obs_tr)+3)),dtype=np.float32)
   t3 = np.zeros(int(round(len(obs_tr)+3)),dtype=np.float32)
   t1[0:len(obs_tr)] = obs_tr[0:len(obs_tr)] 
   t2[0:len(obs_tr)] = obs_empty_tr[0:len(obs_tr)]
   t3[0:len(obs_tr)] = syn_empty_tr[0:len(obs_tr)]

   m = 100 
   x = fft(t1)
   #for j in range(0,l):
   #   if 100*abs(x[j]) < max(abs(x)):
   #      x[j] = max(abs(x))/100
   if i==50:
      plt.figure(1)
      plt.plot(x[0:m].real)
   y = fft(t2)
   #for j in range(0,l):
   #   if 100*abs(y[j]) < max(abs(y)):
   #      y[j] = max(abs(y))/100
   if i==50:
      plt.figure(2)
      plt.plot(y[0:m].real)
   z = fft(t3)
   if i==50:
      plt.figure(3)
      plt.plot(z[0:m].real)
   data_tr=ifft((z/y)*x)
   if i==50:
      plt.figure(4)
      plt.plot(((z/y)*x)[0:m].real)
      print ((z/y)*x)[0:m].real
      print fft(target)[0:m].real
      #plt.figure(5)
      plt.plot(fft(target)[0:m].real)
      plt.figure(6)
      plt.plot(((z/y)*x)[0:m].real-fft(target)[0:m].real)
      plt.show()
   output[i].data = data_tr[0:len(obs_tr)].real
   output[i].stats.delta=0.01
output.write('specfem2d/data/preprocessed_data.su',format='SU')
