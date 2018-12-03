
import sys

from getpass import getuser
from os.path import abspath, exists
from uuid import uuid4
from seisflows.tools import unix
from seisflows.tools.tools import call, findpath
from seisflows.config import ParameterError, custom_import

PAR = sys.modules['seisflows_parameters']
PATH = sys.modules['seisflows_paths']


class tigergpu(custom_import('system', 'slurm_lg')):
    """ Specially designed system interface for tiger.princeton.edu

      See parent class for more information.
    """

    def check(self):
        """ Checks parameters and paths
        """
        # where job was submitted
        if 'WORKDIR' not in PATH:
            setattr(PATH, 'WORKDIR', abspath('.'))

        # where temporary files are written
        if 'SCRATCH' not in PATH:
            setattr(PATH, 'SCRATCH', PATH.WORKDIR+'/'+'scratch')

        # number of cores per node
        if 'NODESIZE' not in PAR:
            setattr(PAR, 'NODESIZE', 16)

        super(tigergpu, self).check()


    def submit(self, workflow):
        """ Submits workflow
        """
        # create scratch directories
        if not exists(PATH.SCRATCH):
            path = '/scratch/gpfs'+'/'+getuser()+'/'+'seisflows'+'/'+str(uuid4())
            unix.mkdir(path)
            unix.ln(path, PATH.SCRATCH)

        unix.mkdir(PATH.SYSTEM)

        # create output directories
        unix.mkdir(PATH.OUTPUT)
        unix.mkdir(PATH.WORKDIR+'/'+'output.slurm')

        self.checkpoint()

        # prepare sbatch arguments
        call('sbatch '
                + '%s ' % PAR.SLURMARGS
                + '--job-name=%s ' % PAR.TITLE
                + '--output %s ' % (PATH.WORKDIR+'/'+'output.log')
                + '--ntasks-per-node=28 '
                + '--ntasks=28 '
                + '--gres=gpu:4 '
                + '--nodes=%d ' % 1
                + '--time=%d ' % PAR.WALLTIME
                + findpath('seisflows.system') +'/'+ 'wrappers/submit '
                + PATH.OUTPUT)




    def job_array_cmd(self, classname, funcname, hosts):
        return ('sbatch '
                + '%s ' % PAR.SLURMARGS
                + '--job-name=%s ' % PAR.TITLE
                + '--nodes=1 '
                + '--ntasks-per-node=1 '
                + '--ntasks=1 ' 
                + '--gres=gpu:1 '
                + '--time=%d ' % PAR.TASKTIME
                + self.job_array_args(hosts)
                + findpath('seisflows.system') +'/'+ 'wrappers/run '
                + PATH.OUTPUT + ' '
                + classname + ' '
                + funcname + ' '
                + PAR.ENVIRONS)

