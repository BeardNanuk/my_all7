classdef objAScan < hgsetget
  %OBJASCAN Instance of this class holds all parameters of an A-Scan
  %except the raw data.
  %
  %   See readme.txt for a general description of the D-BUS Acquisition
  %   software and structure.
  
  % 9/23/2014 - Bastiaan Dekker
  
  % Copyright 2014, DELFT UNIVERSITY OF TECHNOLOGY.
  
  properties
    dateTime;
    dataFilePath;
    deadAScan;
    waterTemp;
    Points;
    XIncrement;
    XOrigin;
    XReference;
    Delay;
    YIncrement;
    YOrigin;
    YReference;
    srcAngle;
    recAngle;
    srcNr;
    recNr;
    srcRadius;
    recRadius;
    srcX;
    recX;
    srcY;
    recY;
    axisPhantomPos;
    axisArmPos;
  end
  
  methods
    function aScan = objAScan()
      % Constructor
      aScan.deadAScan = false;
    end
    
    function GetInfoFromWaveForm(aScan, waveform)
      % Copy the info from a wavefrom to the properties of this AScan
      % object.
      
      % From the scope readout script:
      %    FORMAT        : int16 - 0 = BYTE, 1 = WORD, 2 = ASCII.
      %    TYPE          : int16 - 0 = NORMAL, 1 = PEAK DETECT, 2 = AVERAGE
      %    POINTS        : int32 - number of data points transferred.
      %    COUNT         : int32 - 1 and is always 1.
      %    XINCREMENT    : float64 - time difference between data points.
      %    XORIGIN       : float64 - always the first data point in memory.
      %    XREFERENCE    : int32 - specifies the data point associated with
      %                            x-origin.
      %    YINCREMENT    : float32 - voltage diff between data points.
      %    YORIGIN       : float32 - value is the voltage at center screen.
      %    YREFERENCE    : int32 - specifies the data point where y-origin
      %                            occurs.
      
      aScan.Points      = waveform.Points;
      aScan.XIncrement  = waveform.XIncrement;
      aScan.XOrigin     = waveform.XOrigin;
      aScan.XReference  = waveform.XReference;
      aScan.Delay       = waveform.Delay;
      
      aScan.YIncrement  = waveform.YIncrement;
      aScan.YOrigin     = waveform.YOrigin;
      aScan.YReference  = waveform.YReference;
    end
    
    function GetInfoFromScan(aScanInfo, scan, iCoord)
      % Copy and calculate the correct properties of this AScan from
      % the corresponding scan and coordinate.
      
      % Copy info directly available from scan object
      aScanInfo.axisPhantomPos  = scan.axisPhantomPos(iCoord);
      aScanInfo.axisArmPos      = scan.axisArmPos(iCoord);
      aScanInfo.srcRadius       = scan.srcRadius;
      aScanInfo.recRadius       = scan.recRadius;
      aScanInfo.srcNr           = scan.coordSrcNr(iCoord);
      aScanInfo.recNr           = scan.coordRecNr(iCoord);
      aScanInfo.srcAngle        = scan.srcAngles(iCoord);
      aScanInfo.recAngle        = scan.recAngles(iCoord);
      
      % Also save the positions
      aScanInfo.srcX = scan.srcRadius*cos(aScanInfo.srcAngle*(pi/180));
      aScanInfo.srcY = scan.srcRadius*sin(aScanInfo.srcAngle*(pi/180));
      aScanInfo.recX = scan.recRadius*cos(aScanInfo.recAngle*(pi/180));
      aScanInfo.recY = scan.recRadius*sin(aScanInfo.recAngle*(pi/180));
      
    end
    
    function SetDateTimeNow(aScan)
      % Set current time in this aScan.
      aScan.dateTime = now;
    end
  end
  
  methods(Static)
    function timeStamps = ConvertTimeStrToNumber(timeStrings)
      timeStamps = datenum(timeStrings, objDBusData.strDateTimeFormat);
    end
  end
end

