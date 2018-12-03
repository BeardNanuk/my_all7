#!/bin/bash
REP=$1
variable=$2

Nit=`wc -l ./output.stats/misfit | cut -f1 -d' '`
Nloop=$(($Nit/10+1))


echo $REP $model_or_grad $variable $name 

for i in `seq 0 $Nloop`;do
for j in `seq 1 10` ;do
k=$((10*$i+$j)) 
           if [ "$k" -gt "$Nit" ]
           then
             break  # Skip entire rest of loop.
           fi
           K="$(printf "%04d" $k)"
           cp $REP/model_true/*_[xz].bin $REP/output/model_$K
           python $REP/plotbin $REP/output/model_$K $REP/Images/$variable/model/It$K $variable  >> xxx &
           ./plot_grad_and_diff $k $variable $REP/Images/$variable/analyse/It$K >> xxx &
      done
wait
      done


