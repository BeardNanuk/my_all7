#!/usr/bin/env python

import sys
import obspy
import numpy as np
from seisflows.plugins import adjoint, misfit, readers, writers
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
from obspy.core import Stream, Trace

# define seismic data reader and writer
reader = getattr(readers,'su')
writer = getattr(writers, 'su')

#plot data
plot=1
plt_num = 10

data1 = reader('specfem2d/data/','data1.su')
data2 = reader('specfem2d/data/','data2.su')
output = reader('specfem2d/data/','data_diff.su')

output = data2.copy()

#statistics
# we make stats only on significant portions of the data : if the data is below 1/10000 of the max of the trace, we don't use it
stats=1
tol=0.00001
num_traces = len(data1)
NSTEP = len(data1[0].data)
vec_stat = np.zeros(num_traces)

for i in range(0,num_traces):
   #data1[i].taper(max_percentage=0.05,type='hann')
   output[i].data = data1[i].data - data2[i].data 
   output[i].stats.delta=0.01
   max1 = max(abs(data1[i].data))
   max2 = max(abs(data2[i].data))
   
   max_diff = max(abs(output[i].data))
   print ''
   print 'trace ' + str(i) 
   print 'Max 1st sample : ' + str(max1)
   print 'Max 2nd sample : ' + str(max2) 
   print 'Max discrepancy (infinite norm) : ' +  str(max_diff)
   print 'Ratio of infinite norms : ' +  str(max_diff/min(max1,max2))
   if (plot == 1):
    if (i % plt_num == 0):
      plt.plot(data1[i].data, label='data1')
      plt.plot(data2[i].data, label='data2')
      plt.plot(output[i].data,label='difference')
      plt.legend(['data1','data2','difference'])
      plt.show()

#   if (stats == 1):
#     max12 = tol * min(max1,max2)
#     n_dat = 0 
#     for j in range(0,NSTEP):
#         if ( min(abs(data1[i].data[j]),abs(data2[i].data[j])) > max12 ) :
#           vec_stat[i] =  abs( output[i].data[j] / max(abs(data1[i].data[j]),abs(data2[i].data[j])) )
#           print  output[i].data[j] , data1[i].data[j], data2[i].data[j], vec_stat[i]
#           n_dat += 1
#     if (n_dat > 0):
#       vec_stat[i] /= n_dat
#     print 'Ecart standard : ' + str(vec_stat[i]*100) + ' %, based on ' + str(n_dat) + ' evaluation points'

#if (plot == 1):
# if (stats == 1):
#   plot(vec_stat)

output.write('specfem2d/data/data_diff.su',format='SU')

















