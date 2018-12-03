% load the parameters for 2D_CSIC_UCM_USCT


% created on Mon Oct 15 13:52:56 UTC 2018
% created by Jiaze He 

i = 1; %j = 6; 
k = 8; %l = 1;
filename = sprintf('Fan%02d_SRC%02d_all.mat',i,k);
eval(['load ', filename, ' mystation';]);





flag_define_para = 1 
flag_assign_value = 2 % 1:using passed-in values from para; 2: define-directly 
flag_source_shape = 1 % 1 point 2 line 
flag_station_shape = 11 % 1 line 2 circle 11 predefined RecPos





if flag_define_para == 1 
% set the basic constants (if not loading from somewhere)
    para.f0=500000; 
    para.fmax = 1000000;
    para.dt = 1e-8;
    para.NRec = 450;
end 


if flag_assign_value == 1 
    f0=para.f0; 
    fmax=para.fmax;
    dt = para.dt;
    NRec = para.NRec;
elseif flag_assign_value == 2 
    % define values here
    
    %%%%%% assign the values related to the source time function (stf)
    f0=3500000; 
    fmax=1000000;
    dt = 1e-8;
    NRec = 450;

    %%%%%%%%%%%%%% parameters related to media and transducers %%%%%%%
    tank_half = 0.02;
    transducer_number = 1; 
    transducer_length=0.004;
    deltaL = transducer_length/(transducer_number-1);
    source_center_x = mystation.xea;
    source_center_y = mystation.yea;
    
    %%%%%%%%%%%%%%%%%%%%%%% parameters related to receivers %%%%%%%%%%
    r = 0.008;
    rec_x_center = 0.0004 * 5-0.00001;
    rec_y_center = 0.02;
    
end

matrix_s_num = [1];

% medium dimensions







    


