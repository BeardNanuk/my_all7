
## data loading for specfem2d  

import numpy as np
# for file finding
import scipy.io as sio
import glob

## input environment variable 
import os

flag_exp_data = int(os.environ['flag_exp_data'])


import pickle
# pickle.dump(exp_para,open('obf/input/data_para.pickle','wb'))
with open('obf/input/data_para.pickle', 'rb') as pickle_file:
     data_para = pickle.load(pickle_file)

flag_seismotype = int(os.environ['flag_seismotype'])

print('flag_seismotype is ',flag_seismotype )

#flag_seismotype = 4

if flag_seismotype != 4:
   Ux_data = data_para.Ux_data
   Uz_data = data_para.Uz_data
   Un_data = data_para.Un_data
else:
## use Un to represent Up as the syc
   Un_data = data_para.Up_data

if flag_exp_data == 1:
   Ue_data = data_para.Ue_data




