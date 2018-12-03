%flag_full_scan and flag_filter cannot be turned on together on paris
flag_filter  = 0; 
flag_figure  = 0; 
flag_full_scan =0;

% load paramters for USCT 
lload;
% filtering the signal again, if flag_filter  = 1;
lfilter;
% figure for all the signals
lfigure;
% write the two column source signal file as ascii  
lsignal_itself_regenerate;
%
l_STATIONS_perscan_regenerate;
%
l_SOURCE_file_regenerate;
%

 


