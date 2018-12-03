#!/bin/sh

## declare an array variable
declare -a arr=("ruined_40%/" "ruined_50%/" "ruined_60%/" "ruined_70%/" "ruined_80%/" "ruined_90%/" "ruined_100%/" )

## now loop through the above array
for i in "${arr[@]}"
do
  sed -i "s:DATA = '/data1/etienneb/2D_inversion_80_elem/Donnees.*:DATA = '/data1/etienneb/2D_inversion_80_elem/Donnees_$i':g" ./paths.py
  echo "$i"
  sfclean
  sfrun
  ./sauve_simu_et_transfert.sh $i
   # or do whatever with individual element of the array
done
