# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
export PATH="$PATH:$HOME/Desktop/my_files/my_bin"
export PATH="$PATH:$HOME/Desktop/my_files/my_bin/files"
export PATH="$PATH:$HOME/Desktop/my_files/my_bin/websites"
export PATH="$PATH:$HOME/Desktop/my_files/my_bin/folders"
export PATH="$PATH:$HOME/Desktop/my_files/alljh/dfiles"


#export PATH="$PATH:/usr/local/anaconda2/bin"

#source /opt/rh/rh-python36/enable
export PATH=$PATH:/home/jiazeh/seisflows/scripts
export PYTHONPATH=$PYTHONPATH:/home/jiazeh/seisflows
export PYTHONUNBUFFERED=1
#module load openmpi/intel-18.0/3.0.0/64
#module load intel/18.0/64/18.0.2.199
module load openmpi/intel-16.0/1.10.2/64
module load intel/16.0/64/16.0.4.258

. /usr/local/anaconda2/etc/profile.d/conda.sh

conda activate obspy

