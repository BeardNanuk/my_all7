classdef objDBusData
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %
  %objDBusData Class containing all functionality and parameters used to
  %   load data for the DBUS acquisition software.
  %   Each recording (A-scan) is saved as a binary file containing the
  %   raw u-int16 oscilloscope data.
  %
  %   All other values and information about an A-scan are saved in two
  %   ways:
  %       1) In a single xml 'header file' with the same name as the
  %       binary file (TODO) 2) The parameters are added to 'log files'
  %       located in the main data directory.
  %
  %   Example: The temperature that was measured during an A-Scan is
  %   saved (1) somewhere within xml header file associated with the
  %   A-scan, and (2) is also added as a line in the 'log file'
  %   'Temperature.txt'.
  %
  %   With big scans the log files might be much faster to process, while
  %   the individual A-scan header files are usefull when looking at a
  %   single A-scan.
  %
  %
  %   Copyright 2014, DELFT UNIVERSITY OF TECHNOLOGY.
  %
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  
  properties (Constant)
    % These properties define how the data is being saved
    
    % How is the raw data saved?
    strRawDataPrecision     = 'uint16';
    strDataFolderName       = 'Data';
    strLogFolderName        = 'Logs';
    
    % How is the data saved in log-files?
    strNewLine              = '\r\n';
    strDateTimeFormat       = 'dd-mm-yyyy-HH:MM:SS';
    strDoubleFormatSpec     = '%1.15e';
    strIntFormatSpec        = '%d';
    
    % What are the log files? What property of objAScan is saved in
    % them? And what is the datatype?
    columnFileName          = 1;
    columnAScanPropertyName = 2;
    columnDataType          = 3;
    logFiles = {...
      'DateTime.txt',         'dateTime',         'datetime'; ... % Timestamp of the moment the waveform was recorded
      'DataFile.txt',         'dataFilePath',     'string'; ...   % Relative path to the binary data file
      'DeadAScan.txt',        'deadAScan',        'int'; ...      % Indicates whether measurement was succesfull or should be disregarded
      'Temperature.txt',      'waterTemp',        'double'; ...   % Measured temperature of the water tank
      'Points.txt',           'Points',           'int'; ...      % Number of data points acquired by the oscilloscope
      'XIncrement.txt',       'XIncrement',       'double'; ...   % Time step between the data points (see also the oscilloscope reading script)
      'XOrigin.txt',          'XOrigin',          'double'; ...   % Time value at x-origin (see also the oscilloscope reading script)
      'XReference.txt',       'XReference',   	  'double'; ...   % Sample number specifying x-origin (see also the oscilloscope reading script)
      'Delay.txt',            'Delay',            'double'; ...   % Temporal offset  (see also the oscilloscope reading script)
      'YIncrement.txt',       'YIncrement',       'double'; ...   % Voltage increment  (see also the oscilloscope reading script)
      'YOrigin.txt',          'YOrigin',          'double'; ...   % Voltage at y-origin  (see also the oscilloscope reading script)
      'YReference.txt',       'YReference',       'double'; ...   % Sample number specifying y-origin  (see also the oscilloscope reading script)
      'SrcAngle.txt',         'srcAngle',         'double'; ...   % Calculated angle between source and image.
      'RecAngle.txt',         'recAngle',         'double'; ...   % Calculated angle between receiver and image.
      'SrcNr.txt',            'srcNr',            'int'; ...      % Number of the source in the image coordinate system.
      'RecNr.txt',            'recNr',            'int'; ...      % Number of the receiver in the image coordinate system.
      'SrcRadius.txt',        'srcRadius',      	'double'; ...   % Radius at which the sources are positioned in the image coordinate system.
      'RecRadius.txt',        'recRadius',      	'double'; ...   % Radius at which the receivers are positioned  in the image coordinate system.
      'SrcX.txt',             'srcX',             'double'; ...   % Calculated X position of the source in the image coordinate system.
      'RecX.txt',             'recX',             'double'; ...   % Calculated X position of the receiver in the image coordinate system.
      'SrcY.txt',             'srcY',             'double'; ...   % Calculated Y position of the source in the image coordinate system.
      'RecY.txt',             'recY',             'double'; ...   % Calculated Y position of the receiver in the image coordinate system.
      'AxisPhantPos.txt',     'axisPhantomPos',  	'double'; ...   % Position of the rotating phantom axis in degrees
      'AxisArmPos.txt',       'axisArmPos',       'double'; ...   % Position of the rotating transducer axis in degrees
      };
    
    % Formulas for calculating the correct waveform are: (See also the oscilloscope reading script)
    % t = XIncrement.*(1:nSamples) - XIncrement.XReference + XOrigin;
    % V = (rawData - YReference).* YIncrement + YOrigin;
    
  end
  
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  methods (Static)
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    function rawData = ReadRawDataCompact(dir, dataFilePaths, nFile)
      % Reads binary data files containing the raw 16bit oscilloscope data.
      nFiles  = length(dataFilePaths);
      
      rawData = cell(nFiles,1);
      
      iFile   = nFile;
      fileID  = fopen(fullfile(dir, dataFilePaths{iFile}));
      
      if fileID ~= -1
        rawData{iFile} = fread(fileID, ...
          [objDBusData.strRawDataPrecision, '=>', ...
          objDBusData.strRawDataPrecision]);
        
        fclose(fileID);
      else
        strWarning = strcat('Unable to open the file :', fullfile(dir, dataFilePaths{iFile}));
        warning(strWarning);
      end
      
    end
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    function [V_downsample, t] = ReadScanWaveformsDownSample(dir, aScansInfo, Downsample)
      % Obtains the voltages and of a complete scan.
      % This function reads the raw binary oscilloscope data.
      % Combined with the given aScansInfo object it calculates the waveform.
      nAScans         = length(aScansInfo.dataFilePath);
      nSamples        = double(aScansInfo.Points(1));
      V_downsample    = zeros(nSamples/Downsample, nAScans);
      t               = (double(aScansInfo.XIncrement(nAScans))*double(Downsample) ...
        .* ( (1:nSamples/Downsample) - double(aScansInfo.XReference(nAScans))) ) ...
        + double(aScansInfo.XOrigin(nAScans));
      % Read raw data
      h = waitbar(0,'Please wait while reading A-scans ...');
      for iAScan = 1:nAScans
        waitbar(iAScan/nAScans,h)
        rawData = objDBusData.ReadRawDataCompact(dir, aScansInfo.dataFilePath, iAScan);
        if ~isempty(rawData{iAScan})
          V = (double(rawData{iAScan}) - double(aScansInfo.YReference(iAScan))) ...
            .* aScansInfo.YIncrement(iAScan) + aScansInfo.YOrigin(iAScan);
        end
        V_fft                   = fftshift(fft(V));
        cutoff1                 = length(V_fft)/2 - length(V_fft)/(2*Downsample) + 2;
        cutoff2                 = length(V_fft)/2 + length(V_fft)/(2*Downsample);
        Window_fft              = cat(1, 0, V_fft(cutoff1:cutoff2));
        V_downsample(:,iAScan)  = ifft(ifftshift(Window_fft))/Downsample;
      end
      close(h)
      
    end
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    function [aScansInfo] = ReadLogFiles(dir)
      % Reads the log files of a complete scan and returns the
      % parameters of the ascans in an objAScan-object.
      
      % The object in which the a-scans are stored.
      aScansInfo = objAScan();
      % We use arrays within a single object because we have will then have much
      % less memory and spead overhead with respect to an array of
      % objects.
      
      % Check directory
      if ~exist(dir, 'dir')
        error('Directory does not exist.')
      end
      
      % Loop through all log files
      for iLogFile=1:size(objDBusData.logFiles,1)
        % Open the file
        fileID = fopen(objDBusData.GetFullLogFileName(dir, objDBusData.logFiles{iLogFile, objDBusData.columnFileName}), 'r');
        if fileID == -1
          warning(['Unable to open the file ', objDBusData.logFiles{iLogFile, objDBusData.columnFileName}])
          continue;
        end
        
        % Read the value depending on the datatype
        strDataType = objDBusData.logFiles{iLogFile, objDBusData.columnDataType};
        values = [];
        if strcmp(strDataType, 'datetime')
          [values]  = textscan(fileID, ['%s', objDBusData.strNewLine]);
          values    = values{1};
        elseif strcmp(strDataType, 'double')
          values    = textscan(fileID, '%f64', 'delimiter', objDBusData.strNewLine);
          values    = values{1};
        elseif strcmp(strDataType, 'int')
          values    = textscan(fileID, objDBusData.strIntFormatSpec, 'delimiter', objDBusData.strNewLine);
          values    = values{1};
        elseif strcmp(strDataType, 'string')
          [values]  = textscan(fileID, ['%s', objDBusData.strNewLine]);
          values    = values{1};
        end
        
        % Set the corresponding property in the aScansInfo object
        set(aScansInfo, objDBusData.logFiles{iLogFile, objDBusData.columnAScanPropertyName}, values);
        
        % Close the file
        fclose(fileID);
      end
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
  end
  
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  % HELPER FUNCTIONS
  methods (Static)
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    function strFile = GetFullLogFileName(dir, strEndFileName)
      strFileName = strEndFileName;
      strFile = fullfile(dir, objDBusData.strLogFolderName, strFileName);
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
  end
  
end

