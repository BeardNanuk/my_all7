#!/bin/bash

f0=100000
NSTEP=15

rm fonction_cout
touch fonction_cout
smooth=0.00375
sed -i "s:SMOOTH.*:SMOOTH=$smooth:g" ./parameters.py
sed -i "s:RATIO.*:RATIO=0.9:g" ./parameters.py
sed -i "s:START.*:START=5:g" ./parameters.py

cp ../model_init/* ./model_init80/
sfclean
F=$f0

for i in `seq 0 $NSTEP`;
do
sed -i "s:f0.*:f0=$F:g" ./specfem2d/SOURCE_0000*
sed -i "s:F0.*:F0=$F:g" ./parameters.py

for j in `seq 1 2 `;
do

if [ $j -eq 1 ]; then
sed -i "s:NREC.*:NREC=32:g" ./parameters.py
cp ./specfem2d/av_STATIONS_000000 ./specfem2d/STATIONS_000000
cp ./specfem2d/av_STATIONS_000001 ./specfem2d/STATIONS_000001
cp ./specfem2d/av_STATIONS_000002 ./specfem2d/STATIONS_000002
cp ./specfem2d/av_STATIONS_000003 ./specfem2d/STATIONS_000003
cp ./specfem2d/av_STATIONS_000000 ./specfem2d/STATIONS_000004
cp ./specfem2d/av_STATIONS_000001 ./specfem2d/STATIONS_000005
cp ./specfem2d/av_STATIONS_000002 ./specfem2d/STATIONS_000006
cp ./specfem2d/av_STATIONS_000003 ./specfem2d/STATIONS_000007
cp ./specfem2d/av_STATIONS_000000 ./specfem2d/STATIONS_000008
cp ./specfem2d/av_STATIONS_000001 ./specfem2d/STATIONS_000009
cp ./specfem2d/av_STATIONS_000002 ./specfem2d/STATIONS_000010
cp ./specfem2d/av_STATIONS_000003 ./specfem2d/STATIONS_000011

num_it=5
directory="output/model_0005"
else
sed -i "s:NREC.*:NREC=128:g" ./parameters.py
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000000
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000001
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000002
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000003
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000004
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000005
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000006
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000007
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000008
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000009
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000010
cp ./specfem2d/STATIONS ./specfem2d/STATIONS_000011

num_it=13
directory="output/model_0013"
fi
echo 'Iteration ' $i 'phase' $j 
sed -i "s:END.*:END=$num_it:g" ./parameters.py

sfclean
sfclean
sfrun
 while [ ! -f "$directory/proc000000_vp.bin" ]
  do 
    sleep 2
  done

cp $directory/* ./model_init80/
echo 'Iteration ' $i 'phase' $j 'copie'

sed -i "s:parameters =.*:parameters = ['vp']:g" ./plotbin
python -W ignore ./plotbin ./model_init80 test
cp test.png Inversion$F$j.png
echo 'nouvelle image a la frequence ' $F
cat output.optim >> fonction_cout
echo 'Iteration ' $i 'phase' $j 'cat'
done

F=$(echo "($F*1.15)" | bc -l)
smooth=$(echo "($smooth/1.15)" | bc -l)
sed -i "s:SMOOTH.*:SMOOTH=$smooth:g" ./parameters.py

done

