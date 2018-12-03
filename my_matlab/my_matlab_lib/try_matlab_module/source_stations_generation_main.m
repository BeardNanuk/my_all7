%%



clear;clc;
% load the library for source_station_file_generation

libpath = '/home/jiazeh/Desktop/alljh/pfiles/my_matlab_lib/array_gen_sp2d';
addpath(libpath)


folder_for_para="linear_array_inversion/";
% folder_for_para="half_circle_source/";

% paraname='par_para';
% parafullpath=strcat(folder_for_para);
% addpath(parafullpath);
addpath(folder_for_para);
%%% par_para was called from the folder of 'folder_for_para';
par_para;

stations_generation;
source_generation;

rmpath(libpath,folder_for_para)