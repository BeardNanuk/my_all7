WORKFLOW='inversion'    # inversion, migration
SOLVER='specfem2d_new'      # specfem2d, specfem3d
SYSTEM='multicore'   # serial, pbs, slurm
OPTIMIZE='LBFGS'         # base, newton
PREPROCESS='base'       # base
POSTPROCESS='base'      # base
GPU_MODE = False
#SCHEME='NLCG'

MISFIT='Waveform'
MATERIALS='Acoustic'
DENSITY='Constant'

# WORKFLOW
BEGIN=1                # first iteration
END=200
NREC=128
NSRC=4                 # number of sources
SAVEGRADIENT=1        # save gradient how often


# PREPROCESSING
FORMAT='su'   # data file format
CHANNELS='p'            # data channels
NORMALIZE=0             # normalize
BANDPASS=0              # bandpass
MUTE=0                  # mute direct arrival
FREQLO=0.               # low frequency corner
FREQHI=0.               # high frequency corner

MUTECONST=0.            # mute constant
MUTESLOPE=0.            # mute slope
WITH_MPI= True

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


NT=2100         # number of time steps
DT=0.00000002         # time step
F0=1000000

# SYSTEM
NTASK=4               # must satisfy 1 <= NTASK <= NSRC
NPROC=1                 # processors per task
NPROCMAX=4
WALLTIME=1000000# walltime
