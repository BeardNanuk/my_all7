#!/usr/bin/env python

### individual trace preprocessing, just to plot the fft spectrum 

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 


if flag_plot_spectrum is 1:

   fig, (ax0,ax1,ax2,ax3,ax4,ax5,ax6) = plt.subplots(nrows=7)
   
   ax0.plot(xf_obs/1000,np.abs(yf_obs),'-k')
   ax0.set_title('observed - ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax0.set_xlabel('frequency (kHz)')
   
   ax1.plot(xf_Newobs/1000,np.abs(yf_Newobs),'-k')
   ax1.set_title('observed w resampling - ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax1.set_xlabel('frequency (kHz)')
   
   ax2.plot(t_total_obs[t_star_showobs:t_end_showobs],trace_obs[t_star_showobs:t_end_showobs],'k-')
   ax2.set_title('observed - ' + str(obs_name) + ' trace ' + str(trace_num))
   ax2.set_xlabel(r'time ($\mu s$)')


   ax3.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_Newobs[freq_step_starNewobs:freq_step_endNewobs]),'-k')
   ax3.set_title('observed w resampling - zoom-in ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax3.set_xlabel('frequency (kHz)')
  

   ax4.plot(t_total_syn[t_star_showsyn:t_end_showsyn],traceNew_syn[t_star_showsyn:t_end_showsyn],'b-')
   ax4.set_title('synthetic - ' + str(syn_name) + ' trace ' + str(trace_num))
   ax4.set_xlabel(r'time ($\mu s$)')

   ax5.plot(xf_Newsyn[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_Newsyn[freq_step_starNewobs:freq_step_endNewobs]),'-b')
   ax5.set_title('systhetic w resampling - zoom-in ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
   ax5.set_xlabel('frequency (kHz)')



   #ax5.plot(t_total_syn[t_star_showsyn:t_end_showsyn],trace_syn[t_star_showsyn:t_end_showsyn]/max(trace_syn[t_star_showsyn:t_end_showsyn]),'b-')
   ax6.plot(t_total_syn[0:2000],stf_syn[0:2000],'g-')
   ax6.set_title('stf gaussian')
   ax6.set_xlabel(r'time ($\mu s$)')

   plt.tight_layout(rect=[0, 0, 2.5, 3])
   plt.savefig(save_input_stfsff_fn,format='png', dpi=200, bbox_inches='tight') 
   plt.show()
   #plt.close()
   add_slide_ze(save_input_stfsff_fn,total_filename_pptx) 
