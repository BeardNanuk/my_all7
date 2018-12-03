%% generate the SOURCE and STATIONS file

% created the cell array related to locations of the sources 
%%%%%%%%%%% STATIONS creation %%%%%%%%%%%%%%%%%%%%%
% sources/events matrix creation 
stations.flag_station_shape = flag_station_shape;
stations.matrix_s_num = matrix_s_num;
stations.folder_for_para = folder_for_para;
switch flag_station_shape

    case {2,3} 
    stations.r = r;
    stations.x_center = rec_x_center;
    stations.y_center = rec_y_center;
    stations.NRec = NRec;
    stations.delta_degree = 2*pi/NRec;

    case 31 
    % r is the length of the linear array 
    stations.r = r;
    stations.x_center = rec_x_center;
    stations.y_center = rec_y_center;
    stations.NRec = NRec;
    stations.delta_length = r/(NRec -1);
    %stations.delta_degree = 2*pi/NRec;

    
    case 11
    stations.RecPos =mystation.RecPos;    
    
    
end
    
% end
Rectemp = create_STATIONS(stations);
%%%%%%%%%%% STATIONS creation %%%%%%%%%%%%%%%%%%%%%
