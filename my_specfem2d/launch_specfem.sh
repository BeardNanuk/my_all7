#!/bin/sh


rm mesherz solverz 
rm OUTPUT_FILES/*



#NPROC=1
NPROC=`grep ^NPROC DATA/Par_file | cut -d = -f 2 | cut -d \# -f 1 | tr -d ' '`
echo $NPROC


mpirun -n 1 $HOME/specfem2d/bin/xmeshfem2D >> mesherz
mpirun -n $NPROC $HOME/specfem2d/bin/xspecfem2D >> solverz

# $HOME/specfem2d/bin/xspecfem2D >> solverz

        Xint=1.0
        Yint=1000.0
        Clip_percent=90


./savesismo ./OUTPUT_FILES/Up_file_single.su -save=./OUTPUT_FILES/seismo.png -c=$Clip_percent -xint=$Xint -yint=$Yint > /dev/null &

python zconvert_su_to_mat


f0=$(sed -n 1,15p DATA/SOURCE | grep 'f0' | cut -d\= -f2 | tr -d '[:space:]')

intf0=${f0%.*}
echo 'intf0 ='$intf0

#nx=$(sed -n 266,268p DATA/Par_fie | grep 'nx' | cut -d\= -f2 | tr -d '[:space:]')
nx=`grep ^nx DATA/Par_file | cut -d = -f 2 | cut -d \# -f 1 | tr -d ' '`
echo 'nx ='$nx

D_T=`grep ^DT DATA/Par_file | cut -d = -f 2 | cut -d \# -f 1 | tr -d ' '| sed 's/-/\_/g'`
echo 'D_T ='$D_T

NSTEP=$(sed -n 26,28p DATA/Par_file | grep 'NSTEP' | cut -d\= -f2 | tr -d '[:space:]')
echo 'NSTEP ='$NSTEP

foldname_for_results_saving=$(printf "$HOME/data_bk/specfem2d_data/noutput_intf0_${intf0}_nx${nx}_D_T${D_T}_NSTEP${NSTEP}")
echo 'bk path is '$foldname_for_results_saving

        if [ -d "$foldname_for_results_saving" ]; then
        echo 'delete the folder'
        rm -r "$foldname_for_results_saving"
        else
        echo 'make a folder'
        mkdir "$foldname_for_results_saving"
        fi


	wait
        cp -r ./* "$foldname_for_results_saving"/
	wait
        #cp -r OUTPUT_FILES "$foldname_for_results_saving"/ &
 	#cp -r DATA "$foldname_for_results_saving"/ &

echo "copying files has been completed"
. zall_plot_su
wait
xdg-open ./OUTPUT_FILES/zseismo.png

