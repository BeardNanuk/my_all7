#!/usr/bin/env python

##  plot the individual traces to evaluate the inverted source

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 


## required input
#steps_length = 3000
#
#t_star_showsyn = 15000
#t_end_showsyn = steps_length + t_star_showsyn
#
#t_star_showobs = 20500
#t_end_showobs = steps_length + t_star_showobs

amp_yf_ratio_obs_syn=max(np.abs(yf_trace_interp_obs[freq_step_starNewobs:freq_step_endNewobs]))/max(np.abs(yf_trace_inverted_syn[freq_step_starNewobs:freq_step_endNewobs]))
amp_t_ratio_obs_syn=max(np.abs(trace_interp_obs))/max(np.abs(trace_Re_syn))
##print("amp_yf_ratio_obs_syn = ", amp_yf_ratio_obs_syn)
##print("amp_t_ratio_obs_syn = ", amp_t_ratio_obs_syn)


fig, (ax1,ax2,ax3,ax4,ax5,ax6) = plt.subplots(nrows=6)
## result checking 
ax1.plot(t_total_syn[t_star_showsyn:t_end_showsyn],trace_Re_syn[t_star_showsyn:t_end_showsyn],'b-')
ax1.set_title('inverted synthetic - ' + ' trace ' + str(trace_num))
ax1.set_xlabel('time (s)')

ax2.plot(xf_Newsyn[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_trace_inverted_syn[freq_step_starNewobs:freq_step_endNewobs]),'-b')
ax2.set_title('inverted sff ' + str(obs_name) + ' trace ' + str(trace_num) + '- absolute_value')
ax2.set_xlabel('frequency (kHz)')

ax3.plot(t_total_syn[t_star_showobs:t_end_showobs],trace_interp_obs[t_star_showobs:t_end_showobs],'k-')
ax3.set_title('observed - ' + str(obs_name) + ' trace ' + str(trace_num))
ax3.set_xlabel('time (s)')

ax4.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_trace_interp_obs[freq_step_starNewobs:freq_step_endNewobs]),'-k')
ax4.set_title('inverted sff ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')
ax4.set_xlabel('frequency (kHz)')

ax5.plot(t_total_syn[t_star_showsyn:t_end_showsyn],trace_Re_syn[t_star_showsyn:t_end_showsyn]*amp_t_ratio_obs_syn,'b-')
ax5.plot(t_total_syn[t_star_showobs:t_end_showobs],trace_interp_obs[t_star_showobs:t_end_showobs],'k-')
plt.legend(['recovered syn using istf', 'obs'], loc=4) # 4 lower right handside corner
ax5.set_title('inverted synthetic - ' + ' trace ' + str(trace_num))
ax5.set_xlabel('time (s)')


ax6.plot(xf_Newsyn[freq_step_starNewobs:freq_step_endNewsyn]/1000,np.abs(yf_trace_inverted_syn[freq_step_starNewobs:freq_step_endNewobs]*amp_yf_ratio_obs_syn),'-b')
ax6.plot(xf_Newobs[freq_step_starNewobs:freq_step_endNewobs]/1000,np.abs(yf_trace_interp_obs[freq_step_starNewobs:freq_step_endNewobs]),'-k')
ax6.set_xlabel('frequency (kHz)')
#ax4.set_title('inverted sff ' + str(obs_name) + ' trace  ' + str(trace_num) + '- absolute_value')



#ax5.plot(t_total_syn[t_star_showsyn:t_end_showsyn],trace_syn[t_star_showsyn:t_end_showsyn]/max(trace_syn[t_star_showsyn:t_end_showsyn]),'b-')
#ax5.plot(t_total_syn[t_star_showobs:t_end_showobs],trace_obs[t_star_showobs:t_end_showobs]/max(trace_obs[t_star_showobs:t_end_showobs]),'k-')

plt.tight_layout(rect=[0, 0, 1.8, 2.4])

save_evaluate_stfsff_complete_fn = save_evaluate_stfsff_firstpart_fn + 'src01_rec%02d.png' % (trace_num)
#u_receives_signals_fn = 'obf/output/csic/Re_trace_compare_src01_rec%02d.png' % (trace_num)
plt.savefig(save_evaluate_stfsff_complete_fn,format='png', dpi=200, bbox_inches='tight')
#plt.close()
add_slide_ze(save_evaluate_stfsff_complete_fn,total_filename_pptx)


