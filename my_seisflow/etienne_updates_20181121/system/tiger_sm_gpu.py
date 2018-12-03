
import os
import sys

from os.path import abspath, basename, join
from seisflows.tools import unix
from seisflows.tools.tools import call,exists, findpath, saveobj
from seisflows.config import ParameterError, custom_import
from subprocess import Popen

from time import sleep

from seisflows.tools import unix
from seisflows.tools.tools import call, findpath, nproc, saveobj
from seisflows.config import ParameterError, custom_import




PAR = sys.modules['seisflows_parameters']
PATH = sys.modules['seisflows_paths']

class tiger_sm_gpu(custom_import('system', 'tiger_sm')):
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

        super(tiger_sm_gpu, self).check()


    def submit(self, workflow):
        """ Submits workflow
        """
        unix.mkdir(PATH.OUTPUT)
        unix.cd(PATH.OUTPUT)

        self.checkpoint()

#        if not exists(PATH.SUBMIT + '/' + 'scratch'):
 #           unix.ln(PATH.SCRATCH, PATH.SUBMIT + '/' + 'scratch')
        nnodes=1#PAR.NTASK / PAR.NGPU
        call('sbatch '
                + '%s ' %  PAR.SLURMARGS
                + '--job-name=%s '%PAR.TITLE
                + '--output=%s '%(PATH.WORKDIR +'/'+ 'output.log')
                + '--nodes %d ' %nnodes
                + '--ntasks-per-node=%d '%PAR.NGPU
                + '--ntasks-per-socket=%d '%PAR.NGPU
                + '--gres=gpu:%d '%PAR.NGPU 
                + '--time=%d '%PAR.WALLTIME
                + findpath('seisflows.system') +'/'+ 'wrappers/submit '
                + PATH.OUTPUT)


#    def run(self, classname, funcname, hosts='all', **kwargs):
#        """  Runs tasks in serial or parallel on specified hosts
#        """
#        self.checkpoint()
#        self.save_kwargs(classname, funcname, kwargs)


#        if hosts == 'all':
#            call('srun '                    
#                    + '--wait=0 '         
#                    + '--exclusive '
#                    + join(findpath('seisflows.system'), 'wrappers/run ')
#                    + PATH.OUTPUT + ' '
#                    + classname + ' '
#                    + funcname + ' '
#                    + PAR.ENVIRONS)

#        elif hosts == 'head':
            # run on head node
#            call('srun '
#                    + '--wait=0 '
#                    + '--ntasks=1 '
#                    + '--nodes=1 '
#                    + '--exclusive '
#                    + join(findpath('seisflows.system'), 'wrappers/run ')
#                    + PATH.OUTPUT + ' '
#                    + classname + ' '
#                    + funcname)

    def run(self, classname, method, hosts='all', **kwargs):
        """ Executes the following task:
              classname.method(*args, **kwargs)
        """
        self.checkpoint()
        self.save_kwargs(classname, method, kwargs)

        if hosts == 'all':
            running_tasks = dict()
            queued_tasks = range(PAR.NTASK)

            # implements "work queue" pattern
            while queued_tasks or running_tasks:

                # launch queued tasks
                while len(queued_tasks) > 0 and \
                      len(running_tasks) < PAR.NTASKMAX:
                    i = queued_tasks.pop(0)
                    p = self._launch(classname, method, taskid=i)
                    running_tasks[i] = p
                    sleep(0.1)

                # checks status of running tasks
                for i, p in running_tasks.items():
                    if p.poll() != None:
                        running_tasks.pop(i)

                if running_tasks:
                    sleep(0.1)

            print ''

        elif hosts == 'head':
            os.environ['SEISFLOWS_TASKID'] = str(0)
            func = getattr(__import__('seisflows_'+classname), method)
            func(**kwargs)

        else:
            raise KeyError('Bad keyword argument: system.run: hosts')


    ### private methods

    def _launch(self, classname, method, taskid=0):
        env = os.environ.copy().items()
        env += [['SEISFLOWS_TASKID', str(taskid)]]
        self.progress(taskid)

        p = Popen(
            findpath('seisflows.system') +'/'+ 'wrappers/run '
            + PATH.OUTPUT + ' '
            + classname + ' '
            + method,
            shell=True,
            env=dict(env))

        return p



    def hostlist(self):
        with open(PATH.SYSTEM+'/'+'hostlist', 'w') as f:
            call('scontrol show hostname $SLURM_JOB_NODEFILE', stdout=f)

        with open(PATH.SYSTEM+'/'+'hostlist', 'r') as f:
            return [line.strip() for line in f.readlines()]

    def getnode(self):
        """ Gets number of running task
        """
        gid = os.getenv('SLURM_GTIDS').split(',')
        lid = int(os.getenv('SLURM_LOCALID'))
        return int(gid[lid])


    def mpiexec(self):
    #    return 'mpirun -np %d '%PAR.NPROC
    #     return 'mpirun --mca plm isolated --mca ras simulator -n 1'
         return 'srun --wait=0 --ntasks=1 --nodes=1 --gres=gpu:1 '

    def save_kwargs(self, classname, funcname, kwargs):
        kwargspath = join(PATH.OUTPUT, 'kwargs')
        kwargsfile = join(kwargspath, classname+'_'+funcname+'.p')
        unix.mkdir(kwargspath)
        saveobj(kwargsfile, kwargs)


    def progress(self, taskid):
        """ Provides status update
        """
        if PAR.NTASK > 1:
            print ' task ' + '%02d of %02d' % (taskid+1, PAR.NTASK)

    def taskid(self):
        """ Provides a unique identifier for each running task
        """
        return int(os.environ['SEISFLOWS_TASKID'])


