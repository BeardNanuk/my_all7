#!/usr/bin/env python


## save source inversion as txt - first inversion 

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 

## revised on Fri Nov  9 16:49:50 UTC 2018
## trace_number range from 1 to 2. 

if flag_save_inverted_stf is 1:
   import time
   
   save_istf_txt_complete_fn = save_istf_txt_firstpart_fn  + '_trstar%03d_trend%03d' % (inv_trace_num_star,inv_trace_num_end) 
   stf_handle = open(save_istf_txt_complete_fn,"w")
   #stf = open("obf/output/stf_istf_chi_2m_tr80to90","w")
   
   
 
   for i in range(0,Ntsyn):#nstep + delay):
       stf_handle.write("%20.19f " %t_totalNew_obs[i])
       if (flag_istf_using_stack is 1):
          stf_handle.write("%20.19f\n" %stf_inverted_stack_trace_filtered[i] )
       elif (flag_istf_using_stack is 2):
          stf_handle.write("%20.19f\n" %stf_inverted_trace_filtered[i] )
       # to make sure the i/o is correct with the write function
       #print(i)
       time.sleep(0.001)
   


