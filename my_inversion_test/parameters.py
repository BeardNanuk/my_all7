WORKFLOW='inversion'    # inversion, migration
SOLVER='specfem2d_new'      # specfem2d, specfem3d
SYSTEM='multicore'   # serial, pbs, slurm
OPTIMIZE='LBFGS'         # base, newton
PREPROCESS='base'       # base
POSTPROCESS='base'      # base
#SCHEME='NLCG'

MISFIT='Waveform'
MATERIALS='Elastic'
DENSITY='Constant'
ATTENUATION='no'	

# WORKFLOW
BEGIN=1                # first iteration
END=200
NREC=128
NSRC=4                 # number of sources
SAVEGRADIENT=1        # save gradient how often


# PREPROCESSING
FORMAT='su'   # data file format
CHANNELS='x'            # data channels
NORMALIZE=0             # normalize
#MUTE=0                  # mute direct arrival

FILTER='Bandpass'
FREQMIN=10000
FREQMAX=2500000


MUTECONST=0.            # mute constant
MUTESLOPE=0.            # mute slope
#WITH_MPI= True

# POSTPROCESSING
SMOOTH=0
SCALE=6.0e6             # scaling factor
RATIO=0.92
START=1

# OPTIMIZATION
PRECOND=None            # preconditioner type
STEPMAX=15              # maximum trial steps
STEPTHRESH=0.1          # step length safeguard
STEPINIT=0.05


NT=4200         # number of time steps
DT=0.00000001         # time step
F0=1000000

# SYSTEM
NTASK=4               # must satisfy 1 <= NTASK <= NSRC
NPROC=1                 # processors per task
#NTASKMAX=4
NPROCMAX=4
#NGPU=4
WALLTIME=1000# walltime
