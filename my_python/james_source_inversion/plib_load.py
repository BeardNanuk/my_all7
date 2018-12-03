#!/usr/bin/env python

### preparation for source inversion 
## import libraries, load data from estimated Green's functions, represented by the received signals from (relatively wide-banded) Gaussian stf
## observed data from experimental signals  

# created by Jiaze He 
# created on Tue Nov 13 20:43:18 STD 2018


import obspy
import numpy as np
import pandas as pd
from myFormat.data_format import para_struct
from myFormat.ze_plot_summary import textplot,add_slide_ze
from seisflows.tools.graphics import _convert_to_array
from scipy.interpolate import interp1d

## for ploting
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
from seisflows.tools.graphics import plot_section

import argparse,sys


# for filtering
from obspy.signal.filter import bandpass


#### for spectrum plotting
from scipy import signal
#from obspy.signal.util import _npts2nfft
#from obspy.signal.invsim import cosine_sac_taper
from scipy.fftpack import fft, ifft, fftfreq

#%matplotlib inline
#import matplotlib.pyplot as plt
from obspy import read, UTCDateTime
## for i/o
#from obspy import read
import scipy.io as sio 
from obspy.core.stream import Stream
import os  

from scipy import interpolate
import pickle

# generating PPT slides
from pptx import Presentation
from pptx.util import Inches

import h5py
# for ppt slides creation time
import datetime

import textwrap

