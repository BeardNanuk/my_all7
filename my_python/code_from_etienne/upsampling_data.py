import time
import math
import sys
import numpy as np
from seisflows.plugins import adjoint, misfit, readers, writers
from scipy.fftpack import fft, ifft
from scipy.signal import resample
import matplotlib.pyplot as plt
from obspy.core import Stream, Trace
# define seismic data reader and writer
reader = getattr(readers,'su')
writer = getattr(writers, 'su')

#output = Stream()

obs = reader('specfem2d/OUTPUT_FILES/','Up_file_single.su')
l = len(obs[1].data)

output = obs
for i in range(0,len(obs)):

   obs_tr = obs[i].data
   data_tr1 = resample(obs_tr,2100)
   data_tr = np.float32(data_tr1)
#   plt.figure(1)
#   plt.plot(obs_tr)
#   plt.figure(2)
#   plt.plot(data_tr)
#   plt.show()
   output[i].data = data_tr
   output[i].stats.delta=0.01
output.write('specfem2d/OUTPUT_FILES/Up_file_single.su',format='SU')
