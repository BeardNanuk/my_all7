% single signal loading 

%Read and paint ...
% % % clear; clc;

%%%%% para loading 
%Load acquisition parameters
load parametros.mat;
%----- Correct BUG in he vector ------------------------------
%In these datasets, the last emitting element is 128, not 121
if he(end) == 122
    he(end) = 1;
end
%-------------------------------------------------------------
%%%%% para loading 

%Load speed of water
load meas_c.mat


% % % % i = 23; %j = 6; 
% % % % k = 8; %l = 1;
% % % % flag_plot = 2; 


        %Get and plot each A-Scan
%         for k = 1:ne
%             for l = 1:nr  

%for i = 1:N_tx %for each fanbeam

    %Load fanbeam file
    file = sprintf('Fan-Beam%02d.mat',i);
    load(file);
    
    %variables in Fan-Beam file are:
    %
    % Ascans_rx     : A-Scan data for all emitter-receiver pairs
    %                 Size = N_tx x sum(he) x sum(hr) x tacq/(0.025*tsa)
    % activos_rx    : Indexes to emitter active elements
    % activos_tx    : Indexes to receiver active elements
    % centros_3     : Coordinates of the emitter array center (mm)
    % centros_4     : Coordinates of the receiver array centers (mm)
    % coordenadas   : Coordinates of the elements (mm)
    %                 Size = N_rx x sum(he) x sum(hr) x 2 x 2
    
    ne = sum(he); %Number of active elements in emission
    nr = sum(hr); %Number of active elements in reception
    
    xe = squeeze(coordenadas(1,:,1,1,1)); %X Coordinates of emitting array
    ye = squeeze(coordenadas(1,:,1,1,2)); %Y Coordinates of emitting array
    l_total = 0;
    % specfem2d simulation time in s. 
    time_length_in_specfem2d = 28000 * 6e-9;
    % timesteps for this data - (time)/(dt[forploting])
    total_timesteps_for_csic = time_length_in_specfem2d * 1e6/(0.025*tsa);
        
    fan_beam_scan_full = zeros(total_timesteps_for_csic,176);
    travel_time_full = zeros(1,176);
%     manual_delay = 0
    manual_delay = 1550 * 4e-9; 
    manual_delay_steps = manual_delay / (0.025*tsa*1e-6);
   for j=1:N_rx %For each receiving array position
          
        xr = squeeze(coordenadas(j,1,:,2,1)); %X Coordinates of receiving array
        yr = squeeze(coordenadas(j,1,:,2,2)); %Y Coordinates of receiving array   
        XR(:,j) = xr;   
        YR(:,j) = yr;  
        %Get and plot each A-Scan
% % %         for k = 1:ne

            for l = 1:nr              
                l_total =  l_total + 1;  
                ascan = detrend(double(squeeze(Ascans_rx(j,k,l,:)))); %Ascan
                %ascan = double(squeeze(Ascans_rx(j,k,l,:))); %Ascan
                fan_beam_scan(:,l_total) = ascan;
                
                %Time base including acquisition delay
                t = tdlr_sitau(j,k,l) + [0:length(ascan)-1]*(0.025*tsa); 
                travel_time_single = tdlr_w(j,k,l);
                steps_delay = round(tdlr_sitau(j,k,l)/(0.025*tsa)+manual_delay_steps);
                steps_2ndhalf = round(total_timesteps_for_csic - steps_delay - 600);
                
                travel_time_full(:,l_total) = travel_time_single;
                fan_beam_scan_full(:,l_total) = [zeros(steps_delay,1);ascan;zeros(steps_2ndhalf,1)];
                
                if flag_plot ==1
                fig=figure(1);
                title(['Fan-Beam ' num2str(i)]);
                xlabel('x (mm)'); ylabel('y (mm)');

                %Plot array elements
                subplot(1,2,1);
                plot(xe,ye,'r.');hold on;
                plot(xr,yr,'b.');
                rectangle('Position',[-95 -95 95*2 95*2],'Curvature',1);
                title(['i=',num2str(i),' k=',num2str(k)]);
                
                %plot the path between emitter and receiver
                plot([xe(k) xr(l)],[ye(k) yr(l)],'k');        
                axis equal; axis([-100 100 -100 100]);
                hold off;
                
                %plot the received signal in percentage
                subplot(1,2,2); 
                plot(t,ascan/32767*100);                
                xlabel('t (us)');
                ylabel('Amplitude (%)');
                axis([t(1) t(end) -100 100])
                title(['j=',num2str(j),' l=',num2str(l)]);
                pause (0.2);
                figname = sprintf('signal_fan%02drec%02dscan%02drec%02d',i,k,j,l);
                saveas(fig,figname,'tif');
            end %  if flag_plot ==1
%                 drawnow;
                
            end %   for l = 1:nr  
            
% % %         end %for k = 1:ne
   end   %for j=1:N_rx %For each receiving array position

dxmm = 1;
% dxmm = 100/200;
dxm = dxmm * 1e-3;
mystation.fan_beam_number = i;
mystation.src_number = k;

fan_beam_scan_full_cut = fan_beam_scan_full(1750:2700,:);
fan_beam_scan_full_cut_udfilped=flipud(fan_beam_scan_full_cut);

mystation.RecPos = [XR(:)*dxm,YR(:)*dxm];
src_xe=xe(k);
src_ye=ye(k);
mystation.SrcRecDiff = [(XR(:)-src_xe)*dxm,(YR(:)-src_ye)*dxm];
SrcRecAbsDist=vecnorm(mystation.SrcRecDiff,2,2);
mystation.SrcRecAbsDist=SrcRecAbsDist;
Tof=SrcRecAbsDist/1479;
mystation.Tof = Tof;
mystation.SrcRecDiffNorm = mystation.SrcRecDiff./vecnorm(mystation.SrcRecDiff,2,2);
mystation.SrcRecRad= atan(mystation.SrcRecDiffNorm(:,2)./mystation.SrcRecDiffNorm(:,1));
SrcRecDiffNorm = (mystation.SrcRecDiffNorm)';
% mystation.XR = XR(:)/1000;
% mystation.YR = YR(:)/1000; 
mystation.xea = xe(k)*dxm;
mystation.yea = ye(k)*dxm;
% save Fan0_mystation.mat mystation 
% %mystation.fan_beam_scan_full=fan_beam_scan_full;
filename = sprintf('Fan%02d_SRC%02d_para.mat',i,k);
% eval(['save ', filename, ' mystation';]);
save(filename,'mystation','-v7.3');
filename = sprintf('Fan%02d_SRC%02d_mat.mat',i,k);
eval(['save ', filename, ' fan_beam_scan_full';]);
filename = sprintf('Fan%02d_SRC%02d_SrcRecDiffNorm.mat',i,k);
% eval(['save ', filename, ' mystation';]);
eval(['save ', filename, ' SrcRecDiffNorm';]);
% end  for i = 1:N_tx %for each fanbeam
