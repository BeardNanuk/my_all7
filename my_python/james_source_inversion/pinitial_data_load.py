#!/usr/bin/env python

### preparation for source inversion - data load 
## load data from estimated Green's functions, represented by the received signals from (relatively wide-banded) Gaussian stf
## observed data from experimental signals  

# created by Jiaze He 
# created on Fri Nov 16 17:20:50 UTC 2018 

load_para = para_struct('load_para')

flag_syn_type = 1 # 1 for su, 2 for pickle  
load_para.flag_syn_type=flag_syn_type
flag_obs_type = 2 # 1 for su, 2 for matlabi
load_para.flag_obs_type=flag_obs_type

#syn_file='Up_csic_rgauss_chi_f03000000_DT4d_9'
#obs_file='Fan07_SRC08_ts2500_mat'
#obs_file='Fan01_SRC08_mat_12dt'
#synpath='obf/input/Up_csic_rgauss_pres_f03000000_DT4d_9.su'
synpath='obf/input/' + syn_file + '.su'
#synpath='obf/input/Up_csic_rgauss_chi_f03000000_DT4d_9.su'
#synpath='obf/input/data_para_csic_gauss_rvelc_f03000000_DT4d_9.pickle'
obspath='obf/input/' + obs_file + '.mat'

load_para.syn_file=syn_file
load_para.synpath=synpath
load_para.obs_file=obs_file
load_para.obspath=obspath


if flag_obs_type is 1: 
    stream_obs = read('obf/input/Up_delayed_ricker_f0500000.su',format='SU', byteorder='<')
    data_obs = _convert_to_array(stream_obs)
elif flag_obs_type is 2:
    from scipy.io import loadmat
    matfile2=loadmat(obspath)
    data_obs = matfile2['fan_beam_scan_full']
    #type(data_obs)

print('the shape of the observed data: ', data_obs.shape)


if flag_syn_type is 1: 
   stream_syn = read(synpath,format='SU', byteorder='<')
   #stream_syn = read('obf/input/Up_csic_gauss_chi_f03000000_DT4d_9.su',format='SU', byteorder='<')
   data_syn = _convert_to_array(stream_syn)
elif flag_syn_type is 2:
   import pickle
   # pickle.dump(exp_para,open('obf/input/data_para.pickle','wb'))
   with open(synpath, 'rb') as pickle_file:
      data_para = pickle.load(pickle_file)
   data_syn = data_para.Un_data 
print('the shape of the synthetic data: ', data_syn.shape)
print('synpath: ', synpath)
print('obspath: ', obspath)

#stf_csic_rgauss_pres_f02000000_DT4d_9
#stf_csic_corrected_gauss_chi_f03000000_DT4d_9
#### load stf function 
stf_syn_pd = pd.read_csv('obf/input/stf_csic_rgauss_chi_f03000000_DT4d_9',header=None,delim_whitespace=True)
stf_syn_1Dnp = stf_syn_pd.values
stf_syn = stf_syn_1Dnp[:,1]
stf_obs_1Dnp = pd.read_csv('obf/input/stf_delayed_ricker_f0500000',header=None,delim_whitespace=True).values
stf_obs = stf_obs_1Dnp[:,1]

syn_name = 'ricker'
obs_name = 'tbd' # to be determined
load_para.syn_name=syn_name
load_para.obs_name=obs_name

str_savefold = 'src_csic_jp_results'
save_parafile_loaddata = str_savefold + '/para_loaddata.png'
load_para.save_parafile_loaddata=save_parafile_loaddata


total_filename_pptx= str_savefold + '/zauto_results.pptx'
load_para.total_filename_pptx=total_filename_pptx

#textplot(load_para,save_parafile_loaddata,flag_close=0)
prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]
## input title of the first slide the pptx
title.text = " source inversion and evaluation"
## input the date and time as the subtitle
now = datetime.datetime.now()
subtitle.text = now.strftime("%Y-%m-%d %H:%M")
prs.save(total_filename_pptx)
#textplot(load_para,save_parafile_loaddata,flag_close=0)
#textplot(load_para,save_parafile_loaddata,flag_close=0)

save_input_stfsff_fn=str_savefold + '/input_signal_spectrum.png'
load_para.save_one_spectrum_fn=save_input_stfsff_fn

save_tukey_fn=str_savefold + '/tukey_filter.png'
load_para.save_tukey_fn=save_tukey_fn

save_istf_firstpart_fn = str_savefold + '/istf'
load_para.save_istf_firstpart_fn=save_istf_firstpart_fn

save_istf_txt_firstpart_fn = str_savefold + '/z2istf' 
load_para.save_istf_txt_firstpart_fn= save_istf_txt_firstpart_fn 

save_Re_obs_pickledump_fn = str_savefold + '/data_Re_obs.pickle'
load_para.save_Re_obs_pickledump_fn=save_Re_obs_pickledump_fn 

save_exp_para_pickledump_fn = str_savefold + '/exp_para'
load_para.save_exp_para_pickledump_fn=save_exp_para_pickledump_fn

save_load_para_pickledump_fn = str_savefold + '/load_para'
load_para.save_load_para_pickledump_fn=save_load_para_pickledump_fn
pickle.dump(load_para,open(save_load_para_pickledump_fn,'wb'))

textplot(load_para,save_parafile_loaddata,flag_close=0)
add_slide_ze(save_parafile_loaddata,total_filename_pptx)
### load mat data over -v7.3
#with h5py.File('obf/input/Fan01_SRC08_para.mat', 'r') as file:
#    mystation_para = list(file['mystation']) # matrix filename is para 


#execfile('pconstant_setup.py')
#execfile('pstf_inverse_wrap.py')

#execfile('ptraceprepare_wrap.py')


