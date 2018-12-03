
r = 0.005;

x_center = 0.00001;
% x_center = 0.0004-0.00001;

y_center = 0.02;

delta_degree = 2*pi/NRec;

for i = 1:round(NRec/2)


    RecPos(i,1) = x_center + r*sin(delta_degree*i); 
    RecPos(i,2) = y_center -r + r*(1-cos(delta_degree*i));
    RecAngles(i,1) = delta_degree*i;
    RecAngles_degree(i,1) = pi*delta_degree*i;
end



matrix_s_num = [1];
m=length(RecAngles);
sen_col = 0:m-1;
for i_num = 1:length(matrix_s_num)

s_num = matrix_s_num(i_num);    
    
source_filename = sprintf('STATIONS_%06d',i_num-1);
formatSpec = 'S%06d AA %20.19f %20.19f %2.1f %2.1f\n';

fileID = fopen(source_filename,'w');
fprintf(fileID,formatSpec,[sen_col',RecPos(:,:),zeros(m,1),zeros(m,1)]');
fclose(fileID);

%av_source_filename = sprintf('av_STATIONS_%06d',i_num-1);
%fileID_av = fopen(av_source_filename,'w');
%fprintf(fileID_av,formatSpec,[sen_col',squeeze(RecPos(s_num,:,:)+tank_half),zeros(m,1),zeros(m,1)]');
%fclose(fileID_av);
% % % 
% % % if flag_full_scan == 1
% % % fullscan_filename = sprintf('fullscan_fn_%06d.dat',i_num-1);
% % % one_scan_temp = squeeze(FullScan(s_num,:,:));
% % % one_scan = zeros(NRec,N);
% % % 
% % % % % for ik = 1:NRec
% % % % % 
% % % % % filtered_signal_temp = filter(fir_coeff, 1, one_scan_temp(ik,:));
% % % % % one_scan(ik,1:N-order/2) = filtered_signal_temp(order/2+1:N);
% % % % % 
% % % % % end
% % % csvwrite(fullscan_filename,one_scan);
% % % end %flag_full_scan == 1

% % % RecPos_filename = sprintf('RecPos_fn_%06d.dat',i_num-1);
% % % one_shot_angles = squeeze(RecPos(s_num,:,:));
% % % csvwrite(RecPos_filename,one_shot_angles);

end




