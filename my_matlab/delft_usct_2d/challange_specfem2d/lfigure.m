% l figure 


%% plot signals and spectrum with fi

if flag_figure == 1

subrows=4;
subcols=3;

plot_timestep_star = 6000;
plot_timestep_end = 7500;
length_to_display = plot_timestep_end - plot_timestep_star + 1; 

X1=fft(source_time_filtered_function,N)/fs;
absX1=abs(X1);
X1_fftshift=fftshift(X1);
abs_X1_fftshift=abs(X1_fftshift);

X2=fft(filtered_signal,N)/fs;
absX2=abs(X2);
X2_fftshift=fftshift(X2);
abs_X2_fftshift=abs(X2_fftshift);

X3=fft(filtered_signal_no_delay,N)/fs;
absX3=abs(X3);
X3_fftshift=fftshift(X3);
abs_X3_fftshift=abs(X3_fftshift);


ff2=-(fs-fs/N)*0.5:fs/N:(fs-fs/N)*0.5;

plot_range_half=2000;
figure('Position', [100,50,1800,900]);
set(gcf, 'Color', [1,1,1]);
subplot(subrows,subcols,1);
plot(time,source_time_filtered_function_original,'k');
title(['Original sensor 225 td']);
subplot(subrows,subcols,2);
plot(time(plot_timestep_star:plot_timestep_end),...
    source_time_filtered_function_original(plot_timestep_star:plot_timestep_end),'k');
title(['Original sensor 225 td - zoom-in']);
subplot(subrows,subcols,3);
plot(time(plot_timestep_star:plot_timestep_end),...
    source_time_filtered_function(plot_timestep_star:plot_timestep_end),'b');hold on;
plot(time(plot_timestep_star:plot_timestep_end),...
    filtered_signal(plot_timestep_star:plot_timestep_end),'r');
legend('rect winned ','filtered');
title(['Retangular windowed w/ filtered td']);

subplot(subrows,subcols,subcols+1);
plot(time,source_time_filtered_function,'b');
title(['Retangular windowed td']);
subplot(subrows,subcols,subcols+2);
plot(time(plot_timestep_star:plot_timestep_end),...
    source_time_filtered_function(plot_timestep_star:plot_timestep_end),'b');
title(['Retangular windowed td  - zoom-in']);

subplot(subrows,subcols,subcols+3);
plot(time(plot_timestep_star:plot_timestep_end),...
    filtered_signal(plot_timestep_star:plot_timestep_end),'r');
title(['Rect win filt delay adjus td']);


subplot(subrows,subcols,2*subcols+1);
plot(ff2,abs_X1_fftshift,'b');
xlim([ff2(round(N/2)+1-plot_range_half),ff2(round(N/2)+1+plot_range_half)]);
% % % stem(abs_X1_fftshift);
% % % xlim([round(N/2)+1-plot_range_half,round(N/2)+1+plot_range_half]);
title(['Retangular windowed fd']);

subplot(subrows,subcols,2*subcols+3);
plot(ff2,abs_X2_fftshift,'r');
xlim([ff2(round(N/2)+1-plot_range_half),ff2(round(N/2)+1+plot_range_half)]);
% % % stem(abs_X1_fftshift);
% % % xlim([round(N/2)+1-plot_range_half,round(N/2)+1+plot_range_half]);
title(['Retangular windowed & filtered fd']);


subplot(subrows,subcols,3*subcols+1);
plot(source_time_filtered_function,'b');
title(['Retangular windowed - time steps']);

subplot(subrows,subcols,2*subcols+2);
plot(filtered_signal_no_delay,'m');
title(['filtered delay matching for exp']);
subplot(subrows,subcols,3*subcols+2);
plot(time(1:length_to_display),filtered_signal_no_delay(1:length_to_display),'m');
title(['filtered delay matching for exp td']);
subplot(subrows,subcols,3*subcols+3);
plot(ff2,abs_X2_fftshift,'m');
xlim([ff2(round(N/2)+1-plot_range_half),ff2(round(N/2)+1+plot_range_half)]);
title(['filtered delay matching for exp fd']);

end %if flag_figure == 1