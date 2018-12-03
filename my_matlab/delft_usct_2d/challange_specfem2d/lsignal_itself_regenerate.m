%% 
SOURCE_SIGNAL_MATRIX = [time_my',filtered_signal_no_delay(1:length(time_my))];
% % % % dlmwrite('usct_source_func.txt',SOURCE_SIGNAL_MATRIX,'delimiter','\t','precision',20);
%% write two column [time_my,fi]
source_signal_filename = sprintf('filtered_signal_no_delay');

% source_filename = sprintf('SOURCE_%06d',i_num-1);
fileID = fopen(source_signal_filename,'w');
 
for i_num = 1:length(SOURCE_SIGNAL_MATRIX(:,1))
% s_num = matrix_s_num(i_num);    
% source_filename = sprintf('STATIONS_%06d',i_num-1);
if i_num ~= length(SOURCE_SIGNAL_MATRIX(:,1))
formatSpec = '%20.19f \t %20.19f \n';
% formatSpec = '%11.10f \t %20.19f \n';
else
formatSpec = '%20.19f \t %20.19f ';
%      formatSpec = '%11.10f \t %20.19f ';
end
% % % % fileID = fopen(source_filename,'w');
fprintf(fileID,formatSpec,SOURCE_SIGNAL_MATRIX(i_num,:));

%%%%%%%%% adjoint source saving %%%%%%%%%%%%%%%%%%
% av_source_filename = sprintf('av_STATIONS_%06d',i_num-1);
% fileID_av = fopen(av_source_filename,'w');
% fprintf(fileID_av,formatSpec,[sen_col',squeeze(RecPos(s_num,:,:)+tank_half),zeros(m,1),zeros(m,1)]');
% fclose(fileID_av);

end

fclose(fileID);


