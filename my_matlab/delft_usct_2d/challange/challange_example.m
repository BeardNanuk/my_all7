%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   This scripts reads the data covering a 2D scan of an agar based phantom
%   submerged in water.
%   The data is stored in two directories:
%   - emptyscan_450rec      scan with only the transducers being submerged
%                           in water. No object is present, measured at a
%                           single source position.
%   - phantom_45src_450rec  scan of an agar based phantom using 45 source
%                           positions and 450 receiver positions.
%   To read the data, the files objAScan.m and objDBusData.m are needed.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clc; clear all; close all;

fprintf('\n==================[ challange_example.m ]==================\n');
fprintf('\n  This script reads the data and generates a SAFT image.  \n\n');
fprintf(' ');

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   Define paths
PathData      = 'phantom_45src_450rec';     % agar based phantom
PathDataEmpty = 'emptyscan_450rec';         % empty scan

f0            = 0.5E6;                      % center frequency
fmax          = 2.0*f0;                     % "maximum" frequency in signal

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   Read data for scan without an object

% structure containing information about scanning geometry
ScanInfo        = objDBusData.ReadLogFiles(PathDataEmpty);
dt              = mean(ScanInfo.XIncrement);  % temporal step size
dtNew           = 1.0 / (2.0*fmax);           % temporal step size after downsampling
DownSampleFact  = floor(dtNew/dt);
dtNew           = dt*DownSampleFact;
% reading of actual data
[rawdata, time] = objDBusData.ReadScanWaveformsDownSample(PathDataEmpty, ScanInfo, DownSampleFact);

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   Read data for complete scan with object

% structure containing information about scanning geometry
ScanInfo        = objDBusData.ReadLogFiles(PathData);
% reading of actual data
[rawdata, time] = objDBusData.ReadScanWaveformsDownSample(PathData, ScanInfo, DownSampleFact);

% Determine important parameters
% Nt = number of time samples in single trace
% Na = number of A-scans in complete data
[Nt,Na]         = size(rawdata);  

SrcAngles       = sort(unique(round(100*ScanInfo.srcAngle))/100); % angular positions source
RecAngles       = sort(unique(round(100*ScanInfo.recAngle))/100); % angular positions receiver

% Number of Sources and Receivers
NSrc            = length(SrcAngles);
NRec            = length(RecAngles);

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   Reshape the data into the form NSrc x NRec x Nt
%   and select the data for the fortran code
FullScan        = zeros(NSrc,NRec,Nt);
SrcPos          = zeros(NSrc,2);
RecPos          = zeros(NSrc,NRec,2);
PhiRec          = zeros(NSrc,NRec);
PhiSrc          = zeros(NSrc,NRec);

for n = 1:NSrc
  PhiSrc(n,:)         = SrcAngles(n);
  % find A-scans related to particular source angle
  indSrc              = find( round(100*ScanInfo.srcAngle)/100 == SrcAngles(n));
  SrcPos(n,1:2)       = [ScanInfo.srcX(indSrc(1)) ScanInfo.srcY(indSrc(1))];
  % find corresponding receiver angles
  RecAngles           = ScanInfo.recAngle(indSrc);
  % find corresponding A-scans
  BScan               = rawdata(:,indSrc);
  RecPos(n,:,1:2)     = [ScanInfo.recX(indSrc) ScanInfo.recY(indSrc)];
  % sort corresponding receiver angles
  [RecAngles,indRec]  = sort(RecAngles);
  PhiRec(n,:)         = RecAngles;
  RecPos(n,:,1:2)     = RecPos(n,indRec,1:2);
  % fill array FullScan with corresponding A-scans
  for m = 1:length(RecAngles)
    FullScan(n,m,:) = BScan(:,indRec(m));
  end
end

save('data.mat');
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   Generate image of object using delay and sum
load('data.mat');

nx  = 200;
ny  = 200;
x   = linspace( min(ScanInfo.recX(:))/2, max(ScanInfo.recX(:))/2, nx );
y   = linspace( min(ScanInfo.recY(:))/2, max(ScanInfo.recY(:))/2, ny );

c0  = 1490;
chi = zeros(nx,ny);
for n = 1:NSrc
  for m = 1:NRec
    %
    if (abs(PhiSrc(n,m)-PhiRec(n,m))<90)
      AScan = squeeze(FullScan(n,m,:));
      %
      k = 1:nx;
      for kk = 1:ny;
        dist1     = sqrt((SrcPos(n,1) - x(k)).^2+(SrcPos(n,2) - y(kk)).^2);
        dist2     = sqrt((RecPos(n,m,1) - x(k)).^2+(RecPos(n,m,2) - y(kk)).^2);
        dist      = dist1 + dist2;
        time      = floor((dist/c0)/dtNew);
        chi(k,kk) = chi(k,kk) + AScan(time);
      end
      %
    end
    %
  end
end

figure(1); imagesc(y,x,chi); axis image

return
