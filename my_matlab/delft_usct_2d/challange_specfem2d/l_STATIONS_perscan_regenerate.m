%% generate STATIONS,av_STATIONS,fullscan_,RecPos_fn_ files, 



tank_half = 0.02;
% tank_half = 0.75/2;
matrix_s_num = [1];
m=length(RecAngles);
sen_col = 0:m-1;
for i_num = 1:length(matrix_s_num)

s_num = matrix_s_num(i_num);    
    
source_filename = sprintf('STATIONS_%06d',i_num-1);
formatSpec = 'S%06d AA %20.19f %20.19f %2.1f %2.1f\n';

fileID = fopen(source_filename,'w');
fprintf(fileID,formatSpec,[sen_col',squeeze(RecPos(s_num,:,:)+tank_half),zeros(m,1),zeros(m,1)]');
fclose(fileID);

av_source_filename = sprintf('av_STATIONS_%06d',i_num-1);
fileID_av = fopen(av_source_filename,'w');
fprintf(fileID_av,formatSpec,[sen_col',squeeze(RecPos(s_num,:,:)+tank_half),zeros(m,1),zeros(m,1)]');
fclose(fileID_av);

if flag_full_scan == 1


fullscan_filename = sprintf('fullscan_fn_%06d.dat',i_num-1);

FullScanname='lFullScan.mat';
FullScanparafullpath=strcat(folder_to_replicate,FullScanname)
load(FullScanparafullpath);

% load lFullScan.mat;
% Mze = csvread(fullscan_filename);
one_scan_temp = squeeze(FullScan(s_num,:,:));
one_scan = zeros(NRec,N);

for ik = 1:NRec

filtered_signal_temp = filter(fir_coeff, 1, one_scan_temp(ik,:));
one_scan(ik,1:N-order/2) = filtered_signal_temp(order/2+1:N);

end
csvwrite(fullscan_filename,one_scan(:,1:15000));
end %flag_full_scan == 1

RecPos_filename_temp = sprintf('RecPos_fn_%06d.dat',i_num-1);
RecPos_filename = strcat(folder_to_replicate,RecPos_filename_temp);
one_shot_angles = squeeze(RecPos(s_num,:,:));
csvwrite(RecPos_filename,one_shot_angles);

end
