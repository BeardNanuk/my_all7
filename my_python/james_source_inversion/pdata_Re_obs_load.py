#!/usr/bin/env python


## data recovered as numpy as, one is interpolated observed data; the other is received data generated from the inverted source time function 

## created on Tue Nov 13 20:43:18 STD 2018 
## created by Jiaze He

import pickle 

with open(load_load_para_pickleopen_fn,'rb') as handle:
    load_para = pickle.load(handle)

with open(load_para.save_exp_para_pickledump_fn,'rb') as handle:
    exp_para = pickle.load(handle)

with open(save_Re_obs_pickledump_fn,'rb') as handle:
#with open('obf/input/data_Re_obs.pickle','rb') as handle:
    #pipeline1 = pickle.load(handle)
    data_Re_obs = pickle.load(handle)


load_Re_para = para_struct('load_Re_para')
flag_Re_syn_type=1; load_Re_para.flag_Re_syn_type = flag_Re_syn_type

syn_Re_file = 'Up_sp_mid_20181130_istf_fan7_350k_650k_f0500000_DT4d_8'
#syn_Re_file = 'Up_sp_lg_20181130_z2istf_delay_adjusted_trstar090_trend091_abs_chi_f03500000_DT4d_9'
#syn_Re_file = 'Up_csic_tbd_chi_f02000000_DT4d_9'
#syn_Re_file = 'Up_csic_tbd_pres_f02000000_DT4d_9'

sig_comp_folder = str_savefold + '/' + syn_Re_file

if not os.path.exists(sig_comp_folder):
    os.makedirs(sig_comp_folder)

#syn_Re_file = 'Up_csic_tbd_chi_f02000000_DT4d_9'
load_Re_para.syn_Re_file=syn_Re_file
syn_Re_path='obf/input/' + syn_Re_file + '.su'
#syn_Re_path='obf/input/Up_csic_tbd_chi_f02000000_DT4d_9.su'
load_Re_para.syn_Re_path = syn_Re_path
#syn_Re_path='obf/input/Up_csic_tbd_pres_f02000000_DT4d_9.su'
#syn_Re_path='obf/input/data_para_csic_tbd_disp_f02000000_DT4d_9.pickle'


if flag_Re_syn_type is 1:  
   stream_syn = read(syn_Re_path,format='SU', byteorder='<')
   #stream_syn = read('obf/input/Up_csic_gauss_chi_f03000000_DT4d_9.su',format='SU', byteorder='<')
   #data_syn = _convert_to_array(stream_syn)
   data_Re_syn = _convert_to_array(stream_syn)
elif flag_Re_syn_type is 2:
   import pickle
   # pickle.dump(exp_para,open('obf/input/data_para.pickle','wb'))
   with open(syn_Re_path, 'rb') as pickle_file:
      data_para = pickle.load(pickle_file)
   data_Re_syn = data_para.Un_data 

print('data from specfem2d using istf:',syn_Re_path)
print('the shape of the synthetic data: ', data_Re_syn.shape)


save_parafile_loadRedata = sig_comp_folder + '/para_loadRedata.png'
load_Re_para.save_parafile_loadRedata=save_parafile_loadRedata

#save_parafile_loadRedata = str_savefold + '/para_loadRedata.png'
#load_Re_para.save_parafile_loadRedata=save_parafile_loadRedata

save_evaluate_stfsff_firstpart_fn= sig_comp_folder + '/eval_stfsff'
load_Re_para.save_evaluate_stfsff_firstpart_fn=save_evaluate_stfsff_firstpart_fn

save_filterd_data_trace_firstpart_fn = sig_comp_folder + '/filt_data'
load_Re_para.save_filterd_data_trace_firstpart_fn=save_filterd_data_trace_firstpart_fn

textplot(load_Re_para,save_parafile_loadRedata,flag_close=0)
add_slide_ze(save_parafile_loadRedata,total_filename_pptx)



#stream_syn = read(syn_Re_path,format='SU', byteorder='<')
#stream_syn = read('obf/input/Up_csic_gauss_chi_f03000000_DT4d_9.su',format='SU', byteorder='<')


