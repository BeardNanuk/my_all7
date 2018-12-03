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
   fig, (ax0,ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10) = plt.subplots(nrows=11)

   ax0.plot(t_totalNew_obs[NtNewobs-(t_endNew_showobs - t_starNew_showobs):NtNewobs],traceNew_obs_filtered[NtNewobs-(t_endNew_showobs - t_starNew_showobs):NtNewobs],'k-')
   ax0.set_title('obs' + str(obs_name) + ' trace_seleted '+str(trace_seleted))
   ax0.set_xlabel(r'time ($\mu s$)')   

   ax1.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(syn_taper[freq_step_starNewobs:freq_step_endNewobs]),'-r')
   ax1.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_Newsyn_filteredNormsyn[freq_step_starNewobs:freq_step_endNewobs]),'-b')
   ax1.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_Newsyn_filteredNormobs[freq_step_starNewobs:freq_step_endNewobs]),'-k')
   ax1.legend(['Filter for G', 'Obs Data', "Green's Function - filtered syn signal "])
   ax1.set_xlabel('frequency (kHz)')

   ax2.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_stf_inverted[freq_step_starNewobs:freq_step_endNewobs]),'-g')
   ax2.set_title('inverted sff ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax2.set_xlabel('frequency (kHz)')
   
   ax3.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_stf_inverted_stack[freq_step_starNewobs:freq_step_endNewobs]),'-m')
   ax3.set_title('inverted sff stacked ' + str(obs_name)+' star_trace '+str(inv_trace_num_star)+ 'end_trace '+str(inv_trace_num_end) )
   ax3.set_xlabel('frequency (kHz)')
   
   ax4.plot(t_totalNew_obs[t_starNew_showobs:t_endNew_showobs],stf_inverted[t_starNew_showobs:t_endNew_showobs],'g-')
   ax4.set_title('inverted stf - ' + str(obs_name) + ' trace ' + str(trace_num))
   ax4.set_xlabel(r'time ($\mu s$)')
   
   ax5.plot(t_totalNew_obs[t_starNew_showobs:t_endNew_showobs],stf_inverted_stack[t_starNew_showobs:t_endNew_showobs],'m-')
   ax5.set_title('inverted stf - stacked ' + str(obs_name))
   ax5.set_xlabel(r'time ($\mu s$)')

   ax6.plot(t_totalNew_obs[t_starNew_showobs:t_endNew_showobs],stf_inverted_trace_filtered[t_starNew_showobs:t_endNew_showobs],'g-')
   ax6.set_title('inverted stf filtered' + str(obs_name) + ' trace' + str(trace_num))
   #ax6.set_xlabel('time (us)')
   ax6.set_xlabel(r'time ($\mu s$)')

   ax7.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_stf_inverted_trace_filtered[freq_step_starNewobs:freq_step_endNewobs]),'-g')
   ax7.set_title('inverted sff filtered' + str(obs_name) + ' trace' + str(trace_num) )
   ax7.set_xlabel('frequency (kHz)')

   ax8.plot(t_totalNew_obs[t_starNew_showobs:t_endNew_showobs],stf_inverted_stack_trace_filtered[t_starNew_showobs:t_endNew_showobs],'m-')
   ax8.set_title('inverted stf trace filtered' + str(obs_name) + ' star_trace '+str(inv_trace_num_star)+ 'end_trace '+str(inv_trace_num_end))
   ax8.set_xlabel(r'time ($\mu s$)')

   ax9.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_stf_inverted_stacked_trace_filtered[freq_step_starNewobs:freq_step_endNewobs]),'-m')
   ax9.set_title('inverted sff trace filtered' + str(obs_name) + ' star_trace '+str(inv_trace_num_star)+ 'end_trace '+str(inv_trace_num_end))
   ax9.set_xlabel('frequency (kHz)')

   ax10.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_traceNew_obs_filtered[freq_step_starNewobs:freq_step_endNewobs]),'-k')
   ax10.set_title('inverted sff trace filtered' + str(obs_name) + ' star_trace '+str(inv_trace_num_star)+ 'end_trace '+str(inv_trace_num_end))
   ax10.set_xlabel('frequency (kHz)')


   plt.tight_layout(rect=[0, 0, 1.2, 5])
   fig.show()
   save_istf_complete_fn = save_istf_firstpart_fn + 'src01_rec%02d_trstar%03d_trend%03dfmin%d_fmax%d.png' % (trace_num,inv_trace_num_star,inv_trace_num_end,freqmin,freqmax)
   #save_fig_fn= 'obf/output/csic/istf_src01_rec%02d_trstar%03d_trend%03d.png' % (trace_num,inv_trace_num_star,inv_trace_num_end)
   plt.savefig(save_istf_complete_fn,format='png', dpi=200, bbox_inches='tight')
   add_slide_ze(save_istf_complete_fn,total_filename_pptx,width = 4)


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

