#!/bin/bash

# Script de copie et presentation des resultats d'inversion avec Seisflows
# Etienne Bachmann, Juillet 2017


REP='simu'


echo
echo  -e "\033[31m\033[1mSauvegarde de la simulation dans le repertoire $REP ...\033[0m"
echo
rm -rf $REP
mkdir $REP


cp ./output.stats/misfit $REP 
cp ./output.log $REP
gnuplot gnuplot_script 
cp cost_function.png $REP 
mkdir $REP/output $REP/model_init $REP/model_true $REP/specfem_data $REP/traces
cp -R ./output/* $REP/output
cp model_init80/* $REP/model_init
cp model_true80/* $REP/model_true
cp parameters.py $REP
cp specfem2d/* $REP/specfem_data
cp plotbin $REP


# Get various parameters to determine the repository name and the images to process
AC_or_El=`grep ^MATERIALS   ./parameters.py | cut -d = -f 2 | sed 's/ //g'| tr -d \'` 
Density=`grep ^DENSITY   ./parameters.py | cut -d = -f 2 | sed 's/ //g' | tr -d \'`
Nevent=`grep ^NSRC   ./parameters.py | cut -d = -f 2 | sed 's/ //g' | tr -d \'` 
Nit=`wc -l ./output.stats/misfit | cut -f1 -d' '`
Nit="$(printf "%04d" $Nit)"
echo  -e "\033[32m\033[1mSimulation : $AC_or_El\033[0m"
echo  -e "\033[32m\033[1mDensite : $Density\033[0m"
echo  -e "\033[32m\033[1mNombre d iterations : $Nit\033[0m"
echo

echo  -e "\033[31m\033[1mCreation des images des sismogrammes...\033[0m"
echo
# Plot the seismograms
str='Elastic'
Nevent=$(($Nevent-1))
for j in `seq 0 $Nevent` ;do
i="$(printf "%06d" $j)"
if [ "$AC_or_El" == "$str" ]
then
  ./savesismo ./scratch/solver/$i/traces/obs/Ux_file_single.su -save=$REP/traces/obs_disp_x_event_$i.png  > /dev/null &
  ./savesismo ./scratch/solver/$i/traces/obs/Uz_file_single.su -save=$REP/traces/obs_disp_z_event_$i.png > /dev/null &
  ./savesismo ./scratch/solver/$i/traces/syn/Ux_file_single.su -save=$REP/traces/syn_disp_x_event_$i.png > /dev/null &
  ./savesismo ./scratch/solver/$i/traces/syn/Uz_file_single.su -save=$REP/traces/syn_disp_z_event_$i.png > /dev/null &
  ./savesismo ./scratch/solver/$i/traces/adj/Ux_file_single.su.adj -save=$REP/traces/last_adj_disp_x_event_$i.png > /dev/null &
  ./savesismo ./scratch/solver/$i/traces/adj/Uz_file_single.su.adj -save=$REP/traces/last_adj_disp_z_event_$i.png > /dev/null &
else
  ./savesismo ./scratch/solver/$i/traces/obs/Up_file_single.su -save=$REP/traces/obs_event_$i.png > /dev/null &
  ./savesismo ./scratch/solver/$i/traces/syn/Up_file_single.su -save=$REP/traces/syn_event_$i.png > /dev/null &
  ./savesismo ./scratch/solver/$i/traces/adj/Up_file_single.su.adj -save=$REP/traces/last_adj_event_$i.png > /dev/null &
fi
done
wait


echo  -e "\033[31m\033[1mCreation des images du modele et du gradient au fil des iterations...\033[0m"
echo
# Generates images with the iterations
rm -rf $REP/Images 
mkdir $REP/Images $REP/Images/vp $REP/Images/vp/model $REP/Images/vp/analyse

echo  -e "\033[30m\033[1mCreation de modele vp...\033[0m"
./make_pictures.sh $REP  vp > /dev/null 
cp $REP/Images/vp/model/It$Nit.png $REP/vp_resultat_inversion_it_$Nit.png
./plotvp ./model_init80 > /dev/null
cp vp.png $REP/vp_modele_initial.png
./plotvp ./model_true80 >> x
cp vp.png $REP/vp_modele_objectif.png
./plot_abs_diff ./output/model_$Nit ./model_true80/ vp
mv vp_diff_abs_vrai_inverse.png $REP/ 
scale=`grep ^echelle   ./x | cut -d = -f 2 | sed 's/ //g'`
rm x
max_contrast=300
if (( $(echo "$scale > $max_contrast" | bc -l) ));then
  contrast='high'
else
  contrast='low'
fi
echo  -e "\033[32m\033[1mEcart maximum de vitesse : $scale\033[0m"
echo  -e "\033[32m\033[1mContraste considere : $contrast\033[0m"
echo

str='Elastic'
if [ "$AC_or_El" == "$str" ]
then
  mkdir $REP/Images/vs $REP/Images/vs/model $REP/Images/vs/analyse
  echo  -e "\033[30m\033[1mCreation de modele vs...\033[0m"
  ./make_pictures.sh $REP vs > /dev/null 
  cp $REP/Images/vs/model/It$Nit.png $REP/vs_resultat_inversion_it_$Nit.png
  ./plotvs ./model_init80 > /dev/null
  cp vs.png $REP/vs_modele_initial.png
  ./plotvs ./model_true80 > /dev/null
  cp vs.png $REP/vs_modele_objectif.png
  ./plot_abs_diff ./output/model_$Nit ./model_true80/ vs
  mv vs_diff_abs_vrai_inverse.png $REP/  
else
  rm $REP/output/*/*vs.bin
fi

str='Variable'
if [ "$Density" == "$str" ]
then
  mkdir $REP/Images/rho $REP/Images/rho/model $REP/Images/rho/analyse
  echo  -e "\033[30m\033[1mCreation de modele rho...\033[0m"
  ./make_pictures.sh $REP rho > /dev/null 
  echo
  cp $REP/Images/rho/model/It$Nit.png $REP/rho_resultat_inversion_it_$Nit.png
  ./plotrho ./model_init80 > /dev/null
  cp rho.png $REP/rho_modele_initial.png
  ./plotrho ./model_true80 > /dev/null
  cp rho.png $REP/rho_modele_objectif.png
  ./plot_abs_diff ./output/model_$Nit ./model_true80/ rho
  mv rho_diff_abs_vrai_inverse.png $REP/  
else
  rm $REP/output/*/*rho.bin
fi
rm $REP/output/*/*x.bin
rm $REP/output/*/*z.bin


#Write name of output repository
REP2='Resultats_Inversions/2D'

str='Elastic'
if [ "$AC_or_El" == "$str" ]
then
REP2=$REP2'/Elastic'
fi

str='low'
if [ "$contrast" == "$str" ]
then
REP2=$REP2'/Mou/'$1
else
REP2=$REP2'/Dur/'$1
fi

str='Variable'
if [ "$Density" == "$str" ]
then
REP2=$REP2'/with_density'
fi

if [ -n "$2" ]
then              # Tested variable is quoted.
 REP2=$REP2/$2
else
 REP2=$REP2'/simu'
fi

machine=`hostname -s`
machine_to_save='kilianus'

if [ "$machine" == "$machine_to_save" ]
then
  rm -rf /data1/etienneb/$REP2
  mkdir /data1/etienneb/$REP2
else
  ssh $machine_to_save "rm -rf /data1/etienneb/$REP2"
  ssh $machine_to_save "mkdir /data1/etienneb/$REP2"
fi

echo -e "\033[31m\033[1mTransfert de la simulation...\033[0m"
echo
if [ "$machine" == "$machine_to_save" ]
then
  cp -r $REP/* /data1/etienneb/$REP2  > /dev/null
else
  scp -r $REP/* $machine_to_save:/data1/etienneb/$REP2  > /dev/null
fi

echo -e "\033[31m\033[1mCreation des films de l inversion...\033[0m"
echo
str='low'
if [ "$contrast" == "$str" ]
then
  #copie de vp
  if [ "$machine" == "$machine_to_save" ]
  then
    ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/vp/analyse/It%04d.png -vf fps=2 /data1/etienneb/$REP2/vp_film_analyse.mkv
    ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/vp/model/It%04d.png -vf fps=25 /data1/etienneb/$REP2/vp_film_model.mkv
  else
    ssh $machine_to_save "ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/vp/analyse/It%04d.png -vf fps=2 /data1/etienneb/$REP2/vp_film_analyse.mkv &"
    ssh $machine_to_save "ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/vp/model/It%04d.png -vf fps=25 /data1/etienneb/$REP2/vp_film_model.mkv &"
  fi

  #copie de vs
  str='Elastic'
  if [ "$AC_or_El" == "$str" ]
  then
    if [ "$machine" == "$machine_to_save" ]
    then
      ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/vs/analyse/It%04d.png -vf fps=2 /data1/etienneb/$REP2/vs_film_analyse.mkv
      ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/vs/model/It%04d.png -vf fps=25 /data1/etienneb/$REP2/vs_film_model.mkv
    else
      ssh $machine_to_save "ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/vs/analyse/It%04d.png -vf fps=2 /data1/etienneb/$REP2/vs_film_analyse.mkv &"
      ssh $machine_to_save "ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/vs/model/It%04d.png -vf fps=25 /data1/etienneb/$REP2/vs_film_model.mkv &"
    fi
  fi

  #copie de rho
  str='Variable'
  if [ "$Density" == "$str" ]
  then
    if [ "$machine" == "$machine_to_save" ]
    then
      ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/rho/analyse/It%04d.png -vf fps=2 /data1/etienneb/$REP2/rho_film_analyse.mkv
      ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/rho/model/It%04d.png -vf fps=25 /data1/etienneb/$REP2/rho_film_model.mkv
    else
      ssh $machine_to_save "ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/rho/analyse/It%04d.png -vf fps=2 /data1/etienneb/$REP2/rho_film_analyse.mkv &"
      ssh $machine_to_save "ffmpeg -loglevel panic -r 15 -i /data1/etienneb/$REP2/Images/rho/model/It%04d.png -vf fps=25 /data1/etienneb/$REP2/rho_film_model.mkv &"
    fi
  fi

fi
echo  -e "\033[32m\033[1mFin\033[0m"
echo

