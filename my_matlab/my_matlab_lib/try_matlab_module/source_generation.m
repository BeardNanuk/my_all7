
%%%%%%%%%%% SOURCE creation %%%%%%%%%%%%%%%%%%%%%

    src.flag_source_shape = flag_source_shape;
    src.matrix_s_num = matrix_s_num;
    src.transducer_number=transducer_number;
    src.source_center_x = source_center_x;
    src.source_center_y = source_center_y;
    src.f0 = f0;
    src.folder_for_para = folder_for_para;
switch flag_source_shape
    case 2
    %line source
    src.transducer_length=transducer_length;
    src.delta_length = transducer_length/(transducer_number -1);
    src.name_of_source_file = '/home/jiazeh/specfem2d/DATA/rec_to_src/';
    case 1
    src.name_of_source_file = '/home/jiazeh/specfem2d/DATA/';  
    
    case 21
    %line source
    %src.transducer_length=transducer_length;
    %src.delta_length = transducer_length/(transducer_number -1);
    src.name_of_source_file = '/home/jiazeh/specfem2d/DATA/stf_ricker_delayed';
    
    src.r = r;
    src.x_center = rec_x_center;
    src.y_center = rec_y_center;
    src.NRec = length(matrix_s_num);
    src.delta_degree = 2*pi/NRec;

end
SRCtemp = create_SOURCE(src);
%%%%%%%%%%% SOURCE creation %%%%%%%%%%%%%%%%%%%%%

