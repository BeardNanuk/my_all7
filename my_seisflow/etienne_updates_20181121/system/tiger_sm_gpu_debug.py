
import os
import sys

from os.path import abspath, basename, join
from seisflows.tools import unix
from seisflows.tools.tools import call,exists, findpath, saveobj
from seisflows.config import ParameterError, custom_import

PAR = sys.modules['seisflows_parameters']
PATH = sys.modules['seisflows_paths']

class tiger_sm_gpu_debug(custom_import('system', 'tiger_sm')):
    """ An interface through which to submit workflows, run tasks in serial or 
      parallel, and perform other system functions.

      By hiding environment details behind a python interface layer, these 
      classes provide a consistent command set across different computing
      environments.

      For important additional information, please see 
      http://seisflows.readthedocs.org/en/latest/manual/manual.html#system-interfaces
    """

    def check(self):
        """ Checks parameters and paths
        """


        # why does Etienne have it this way?
        if 'NGPU' not in PAR:
            setattr(PAR, 'NGPU', 4)

        super(tiger_sm_gpu_debug, self).check()


    def submit(self, workflow):
        """ Submits workflow
        """
        unix.mkdir(PATH.OUTPUT)
        unix.cd(PATH.OUTPUT)

        self.checkpoint()

#        if not exists(PATH.SUBMIT + '/' + 'scratch'):
 #           unix.ln(PATH.SCRATCH, PATH.SUBMIT + '/' + 'scratch')

        call('sbatch '
                + '%s ' %  PAR.SLURMARGS
                + '--job-name=%s '%PAR.TITLE
                + '--output=%s '%(PATH.WORKDIR +'/'+ 'output.log')
                + '--nodes 1 '
                + '--ntasks-per-node=%d '%PAR.NGPU
                + '--gres=gpu:%d '%PAR.NGPU 
                + '--time=%d '%PAR.WALLTIME
                + findpath('seisflows.system') +'/'+ 'wrappers/submit '
                + PATH.OUTPUT)


    def run(self, classname, funcname, hosts='all', **kwargs):
        """  Runs tasks in serial or parallel on specified hosts
        """
        self.checkpoint()
        self.save_kwargs(classname, funcname, kwargs)

        if hosts == 'all':
            call(findpath('seisflows.system')  +'/'+'wrappers/dsh '
                    + str(PAR.NTASK) + ' '
                    + findpath('seisflows.system')  +'/'+'wrappers/run '
                    + PATH.OUTPUT + ' '
                    + classname + ' '
                    + funcname + ' '
                    + PAR.ENVIRONS)

            #call('srun '                    
            #        + '--wait=0 '         
            #        + '--exclusive '
            #        + join(findpath('seisflows.system'), 'wrappers/run ')
            #        + PATH.OUTPUT + ' '
            #        + classname + ' '
            #        + funcname + ' '
            #        + PAR.ENVIRONS)

        elif hosts == 'head':
            # run on head node
            call(findpath('seisflows.system')  +'/'+'wrappers/run '
                    + PATH.OUTPUT + ' '
                    + classname + ' '
                    + funcname + ' '
                    + PAR.ENVIRONS)

    def hostlist(self):
        with open(PATH.SYSTEM+'/'+'hostlist', 'w') as f:
            call('scontrol show hostname $SLURM_JOB_NODEFILE', stdout=f)

        with open(PATH.SYSTEM+'/'+'hostlist', 'r') as f:
            return [line.strip() for line in f.readlines()]

    def taskid(self):
        """ Gets number of running task
        """
        if os.getenv('SEISFLOWS_TASK_ID'):
            return int(os.getenv('SEISFLOWS_TASK_ID'))
        else:
            return 0
        #gid = os.getenv('SLURM_GTIDS').split(',')
        #lid = int(os.getenv('SLURM_LOCALID'))
        #return int(gid[lid])


    def mpiexec(self):
    #    return 'mpirun -np %d '%PAR.NPROC
 #        return 'srun -n1 --gres=gpu:1 '
        return 'srun --gres=gpu:1 -n 1 -N 1 mpirun --mca plm isolated --mca ras simulator -n 1 '
    def save_kwargs(self, classname, funcname, kwargs):
        kwargspath = join(PATH.OUTPUT, 'kwargs')
        kwargsfile = join(kwargspath, classname+'_'+funcname+'.p')
        unix.mkdir(kwargspath)
        saveobj(kwargsfile, kwargs)
