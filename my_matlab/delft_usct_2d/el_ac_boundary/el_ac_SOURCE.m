%% generate the SOURCE file

tank_half = 0.02;
transducer_number = 1001; 
transducer_length=0.004;
deltaL = transducer_length/(transducer_number-1);


for i_num = 1:length(matrix_s_num)

s_num = matrix_s_num(i_num);    

delta_length = transducer_length/(transducer_number -1);

source_filename = sprintf('SOURCE_%06d',i_num-1);
fileID = fopen(source_filename,'w');

%source_center_x =  0.00001;
source_center_x = 0.0004*5 - 0.00001;
source_center_y = tank_half;
% % % 
% % % SIN=sin(SrcAngles(s_num)/180*pi);
% % % COS=cos(SrcAngles(s_num)/180*pi);


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

    
Bottom_x(iact_each,1)=source_center_x;
Bottom_y(iact_each,1)=source_center_y - 0.5*transducer_length + delta_length*iact_each;    

tempx=Bottom_x(iact_each,1);
tempy=Bottom_y(iact_each,1);

fprintf(fileID,'source_surf = .false. \n');
% source_point_x=transducer_length/transducer_number*iact_each;
xs_str = sprintf('xs = %6.5f \n', tempx);
fprintf(fileID,xs_str);
zs_str = sprintf('zs = %6.5f \n',tempy);
fprintf(fileID,zs_str);
fprintf(fileID,'source_type = 1 \n');
fprintf(fileID,'time_function_type = 1 \n');
name_of_source_file_str = sprintf('name_of_source_file          =  /home/jiazeh/specfem2d/DATA/rec_to_src/ \n',0);
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
