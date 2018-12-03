% lload

%%

folder_to_replicate="p40by40/";
paraname='lpara.mat';
parafullpath=strcat(folder_to_replicate,paraname)
load(parafullpath);
% load('lpara.mat');

f0=para.f0;
fmax = para.fmax;
% steps for specfem2d
output_time_step = 15000; 

dt = para.dt; DownSampleFact=para.DownSampleFact;
dtNew = para.dtNew;fs = para.fs;time = para.time;
timestep_star =para.timestep_star; timestep_end = para.timestep_end;
time_my = para.time_my(1,1:output_time_step);
rawdata2= para.rawdata2;
%source function 
source_time_filtered_function_temp= para.rawdata2(:,225);

%%% about the filters 
half_width=para.half_width;low_freq=para.low_freq;high_freq=para.high_freq;
band=para.band;nyq_freq=para.nyq_freq;band_norm=para.band_norm;
order=para.order;fir_coeff=para.fir_coeff; 
N=para.N;filtered_signal=para.filtered_signal;
filtered_signal_spec=para.filtered_signal_spec;
absfiltered_signal_spec=para.absfiltered_signal_spec;
delay_step_for_exp=para.delay_step_for_exp;
source_time_filtered_function_original= para.source_time_filtered_function_original;
%%% 

SOURCE_SIGNAL_MATRIX=para.SOURCE_SIGNAL_MATRIX;

%%% 
%rawdata = para.rawdata;
SrcAngles=para.SrcAngles;RecAngles=para.RecAngles;
Nt=para.Nt;Na=para.Na;NSrc=para.NSrc;NRec=para.NRec;

SrcPos=para.SrcPos;RecPos=para.RecPos;
%FullScan=para.FullScan;


filtered_signal_no_delay = zeros(N,1);
% %% adjust time steps to matching the arrivals
% % % % delay_step_for_exp = 6600;
% filtered_signal_no_delay(1:end-delay_step_for_exp)= - filtered_signal(delay_step_for_exp+1:end);



