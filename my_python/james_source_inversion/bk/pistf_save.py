#!/usr/bin/env python


## save source inversion as txt - first inversion 

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 

## revised on Fri Nov  9 16:49:50 UTC 2018
## trace_number range from 1 to 2. 

if flag_save_inverted_stf is 1:
   import time
   
   stf = open("obf/output/stf_istf_78_90","w")
   
   for i in range(0,Ntsyn):#nstep + delay):
       stf.write("%20.19f " %t_totalNew_obs[i])
       stf.write("%20.19f\n" %stf_inverted_trace_filtered[i] )
       # to make sure the i/o is correct with the write function
       #print(i)
       time.sleep(0.001)
   


