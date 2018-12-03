%% choose if to do an extra filter 
if flag_filter==1
%% filtering and spectrum 

%%% get the source time function from rawdata2(:,5)
% cutout the main peaks
source_time_filtered_function_temp =source_time_filtered_function_original;
timestep_star = 6787;
timestep_end = 7173;
source_time_filtered_function_temp(timestep_star:timestep_end) = 0;
source_time_filtered_function = source_time_filtered_function_original - source_time_filtered_function_temp;


% filter setup
half_width = 4e5;
low_freq = f0 - half_width;
high_freq = f0 + half_width;
band = [low_freq, high_freq]; % in Herhz 
nyq_freq = fs/2;
band_norm = band / nyq_freq; % in fir1 format - normalized. 

% FIR filter order (i.e. number of coefficients - 1)
order = 2048; % even number only 
 
% Create lowpass FIR filter through a direct approach: provide
% (normalized) cutoff frequency and filter order (assumed as known).
% fir1 takes care of designing the filter by imposing the constraints in
% the frequency domain and transforming back to time using a given window
% (the dafault used here is the Hamming window).
% For more advanced requirements see e.g. firpmord and firpm
% NOTE: fir1, firpmord and firpm all require Signal Processing Toolbox
fir_coeff = fir1(order, band_norm);

% Analyse the filter using the Filter Visualization Tool
hfvt = fvtool(fir_coeff, 'Fs', fs);

% Filter the signal with the FIR filter
filtered_signal_temp = filter(fir_coeff, 1, source_time_filtered_function);
filtered_signal  = zeros(N,1);
filtered_signal(1:end-order/2) = filtered_signal_temp(order/2+1:end);
filtered_signal_spec=fft(filtered_signal,N)/fs;
absfiltered_signal_spec=abs(filtered_signal_spec);
%%% pick a delay manually to bring the received signals to the front
filtered_signal_no_delay = zeros(N,1);
% adjust time steps to matching the arrivals
delay_step_for_exp = 3000;
filtered_signal_no_delay(1:end-delay_step_for_exp)= filtered_signal(delay_step_for_exp+1:end);




end  % if flag_filter==1