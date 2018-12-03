#!/usr/bin/env python


## ploting the inverted stf/sff, with attempts for further improvements using detrend or filtering 

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 

## revised on Fri Nov  9 16:49:50 UTC 2018
## trace_number range from 1 to 2. 


if flag_plot_inverted_stf is 1:

   #stf_inverted=ifft(yf_stf_inverted,n=nfftNewsyn)
   #stf_inverted_stack=ifft(yf_stf_inverted_stack,n=nfftNewsyn)
   
   #fig, (ax1) = plt.subplots(nrows=1)
   fig, (ax1,ax2,ax3,ax4,ax5,ax6,ax7) = plt.subplots(nrows=7)
   
   ax1.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(syn_taper[freq_step_starNewobs:freq_step_endNewobs]),'-r')
   ax1.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_Newsyn_filteredNormsyn[freq_step_starNewobs:freq_step_endNewobs]),'-b')
   ax1.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_Newsyn_filteredNormobs[freq_step_starNewobs:freq_step_endNewobs]),'-k')
   ax1.legend(['Filter for G', 'Obs Data', "Green's Function - filtered syn signal "])

   ax2.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_stf_inverted[freq_step_starNewobs:freq_step_endNewobs]),'-g')
   ax2.set_title('inverted sff ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax2.set_xlabel('frequency (kHz)')
   
   ax3.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_stf_inverted_stack[freq_step_starNewobs:freq_step_endNewobs]),'-m')
   ax3.set_title('inverted sff stacked ' + str(obs_name) )
   ax3.set_xlabel('frequency (kHz)')
   
   ax4.plot(t_totalNew_obs[t_starNew_showobs:t_endNew_showobs],stf_inverted[t_starNew_showobs:t_endNew_showobs],'g-')
   ax4.set_title('inverted stf - ' + str(obs_name) + ' trace ' + str(trace_num))
   ax4.set_xlabel('time (us)')
   
   ax5.plot(t_totalNew_obs[t_starNew_showobs:t_endNew_showobs],stf_inverted_stack[t_starNew_showobs:t_endNew_showobs],'m-')
   ax5.set_title('inverted stf - stacked ' + str(obs_name))
   ax5.set_xlabel('time (us)')

   ax6.plot(t_totalNew_obs[t_starNew_showobs:t_endNew_showobs],stf_inverted_trace_filtered[t_starNew_showobs:t_endNew_showobs],'r-')
   ax6.set_title('inverted stf trace filtered' + str(obs_name))
   ax6.set_xlabel('time (us)')

   ax7.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_stf_inverted_trace_filtered[freq_step_starNewobs:freq_step_endNewobs]),'-r')
   ax7.set_title('inverted sff trace filtered' + str(obs_name) )
   ax7.set_xlabel('frequency (kHz)')

   plt.tight_layout(rect=[0, 0, 1.5, 3])
   fig.show()




#import time
#
#stf = open("obf/output/stf_tbd_csic3","w")
#
#for i in range(0,42000):#nstep + delay):
#    stf.write("%20.19f " %t_totalNew_obs[i])
#    stf.write("%20.19f\n" %stf_inverted_stack[i] )
#    # to make sure the i/o is correct with the write function 
#    #print(i)
#    time.sleep(0.001)
#

