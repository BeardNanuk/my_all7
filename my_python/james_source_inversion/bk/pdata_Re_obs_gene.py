#!/usr/bin/env python


# check the recovered stf's influence, compare the received signals from specfem2d using inverted stf with the measured signals 
# this is to load back the new observed data
## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He


#execfile('pconstant_setup.py')
data_Re_obs=np.zeros((Ntsyn,176))

for trace_num in range(0,176,1):
    execfile('ptraceprepare.py')
    data_Re_obs[:,trace_num] = traceNew_obs[0:Ntsyn] 

##print('shape of data_Re_obs',data_Re_obs.shape)

pickle.dump(data_Re_obs,open('obf/input/data_Re_obs.pickle','wb'))
