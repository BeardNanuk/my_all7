% ltest the txt file wrote 

fileID2 = fopen('filtered_signal_no_delay','r');
formatSpec2 = '%20.19f \t %20.19f';

sizeB= [25000,2];

B = fscanf(fileID2,formatSpec2,sizeB);


fclose(fileID2);

