

function [Rec] = create_STATIONS(src)

%% generate the arrays necessary to create the values in STATIONS file for specfem2d 
% src naming was a bit confusing: should be stations. 

% src=stations
switch src.flag_station_shape
    case 2
    % for full_circle
    for i = 1:round(src.NRec)
        Rec.RecPos(i,1) = src.x_center + src.r*sin(src.delta_degree*i); 
        Rec.RecPos(i,2) = src.y_center -src.r + src.r*(1-cos(src.delta_degree*i));
        Rec.RecAngles(i,1) = src.delta_degree*i;
        Rec.RecAngles_degree(i,1) = pi*src.delta_degree*i;
    end
    case 3
    % for half_circle
    for i = 1:round(src.NRec/2)
        Rec.RecPos(i,1) = src.x_center + src.r*sin(src.delta_degree*i); 
        Rec.RecPos(i,2) = src.y_center -src.r + src.r*(1-cos(src.delta_degree*i));
        Rec.RecAngles(i,1) = src.delta_degree*i;
        Rec.RecAngles_degree(i,1) = pi*src.delta_degree*i;
    end
    
    
    
    case 11
    Rec.RecPos = src.RecPos;

    case 31
    for i = 1:round(src.NRec)
        % horizontal line, rec_center
        Bottom_x(i,1)=src.x_center- 0.5*src.r ...
            + src.delta_length*i;
        Bottom_y(i,1)=src.y_center;    

        Rec.RecPos(i,1)=Bottom_x(i,1);
        Rec.RecPos(i,2)=Bottom_y(i,1);
    end
    
    
end



m=length(Rec.RecPos(:,1));
sen_col = 0:m-1;

for i_num = 1:length(src.matrix_s_num)
% % 
s_num = src.matrix_s_num(i_num);    
    
source_filename = sprintf('STATIONS_%06d',i_num-1);
parafullpath=strcat(src.folder_for_para,source_filename)
formatSpec = 'S%06d AA %20.19f %20.19f %2.1f %2.1f\n';

fileID = fopen(parafullpath,'w');
fprintf(fileID,formatSpec,[sen_col',Rec.RecPos(:,:),zeros(m,1),zeros(m,1)]');
fclose(fileID);

end




