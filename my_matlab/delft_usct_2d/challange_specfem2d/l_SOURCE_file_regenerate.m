%% generate the SOURCE file

transducer_number = 1001; 
transducer_length=0.0254;
deltaL = transducer_length/(transducer_number-1);


for i_num = 1:length(matrix_s_num)

s_num = matrix_s_num(i_num);    

% FullScanname='lFullScan.mat';
% FullScanparafullpath=strcat(folder_to_replicate,FullScanname)
% load(FullScanparafullpath);
source_filename_temp = sprintf('SOURCE_%06d',i_num-1);
source_filename = strcat(folder_to_replicate,source_filename_temp)
fileID = fopen(source_filename,'w');

source_center_x = SrcPos(s_num,1)+tank_half;
source_center_y = SrcPos(s_num,2)+tank_half;

SIN=sin(SrcAngles(s_num)/180*pi);
COS=cos(SrcAngles(s_num)/180*pi);


% SOURCE_file0.write("FORCE  0\n")
% SOURCE_file0.write("time shift:     0.0000")
% SOURCE_file0.write("f0 = %f\n" % f0)
% SOURCE_file0.write("latorUTM: = 0.3\n")
% SOURCE_file0.write("longorUTM: = 0.2\n")
% SOURCE_file0.write("depth: = 0.0\n")
% SOURCE_file0.write("factor force source:             1.d0\n")
% SOURCE_file0.write("component dir vect source E:     0.d0\n")
% SOURCE_file0.write("component dir vect source N:     0.d0\n")
% SOURCE_file0.write("component dir vect source Z_UP:  0.d0\n")
for iact_each = 1:transducer_number

    
Bottom_x=source_center_x + 0.5*transducer_length*SIN;
Bottom_y=source_center_y - 0.5*transducer_length*COS;    

tempx=Bottom_x + iact_each*deltaL*SIN;
tempy=Bottom_y + iact_each*deltaL*COS;

fprintf(fileID,'source_surf = .false. \n');
% source_point_x=transducer_length/transducer_number*iact_each;
xs_str = sprintf('xs = %6.5f \n', tempx);
fprintf(fileID,xs_str);
zs_str = sprintf('zs = %6.5f \n',tempy);
fprintf(fileID,zs_str);
fprintf(fileID,'source_type = 1 \n');
fprintf(fileID,'time_function_type = 8 \n');
name_of_source_file_str = sprintf('name_of_source_file          =  /scratch/gpfs/jiazeh/specfem2d/DATA/stf_cut_3rd_filtered_20000 \n',0);
fprintf(fileID,name_of_source_file_str);
fprintf(fileID,'burst_band_width = 200.415 \n');
fprintf(fileID,'f0 = 500000 \n');
fprintf(fileID,'tshift = 0 \n');
fprintf(fileID,'anglesource = 0.00 \n');
fprintf(fileID,'Mxx = 1.000000 \n');
fprintf(fileID,'Mzz = 1.000000 \n');
fprintf(fileID,'Mxz = 0.000000 \n');
fprintf(fileID,'factor = 1000.000 \n');

end

% fprintf(fileID,formatSpec,[sen_col',squeeze(RecPos(s_num,:,:)),zeros(m,1),zeros(m,1)]');


fclose(fileID);
end
