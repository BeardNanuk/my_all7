#!bin/bash

###
# Things to run after cluster running
# seismo generation, signal in txt, signal in numpy, for signal comparison
. z2ndhalf 

## plot su file to seismo.png
. zall_plot_su 
## old way for generating plots in signals in mat and txt
python zconvert_su_to_mat
## save several seismo signals 
# Specialized script used to visualize seismic section.
python zsavesismo 

## generate a few signals for comparison between syn and obs
. zsu_copy_source

# load Ux Uy in su format, projection then save as numpy array
python zobs_sig_comp
# recover several seismo signals
python zrecover_several_signals
# comparison between experimental data with simulations
python zobs_sig_comp_p2

### backup the important input and output files
# copy the important but limited number of i/o files of specfem2d to /home/jiazeh/temp
. zbksmall




### copying files 
# bk to the $HOME/data_bk/specfem2d_data on this machine
. zcopy_files

## copy cluster files to paris, needs to run zcopy_files first
. zcluster_copy

# headers for files saving
. zpara_headers


### # python version of - from matlab txt filter to source file for specfem2d (also txt)
python zstf_generate


