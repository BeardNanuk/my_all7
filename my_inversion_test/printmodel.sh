#!/bin/bash
rm ./output/model_$1/proc*_x.bin
rm ./output/model_$1/proc*_z.bin
cp model_init/proc0*_x.bin ./output/model_$1
cp model_init/proc0*_z.bin ./output/model_$1
cp ./output/model_$1/proc000000_vp.bin temp
NPROC=0
for i in `seq 1 $NPROC`;
do
str='_x.bin'
cat ./output/model_$1/proc00000$i$str >> ./output/model_$1/proc000000_x.bin
str='_z.bin'
cat ./output/model_$1/proc00000$i$str >> ./output/model_$1/proc000000_z.bin
str='_vp.bin'
cat ./output/model_$1/proc00000$i$str >> ./output/model_$1/proc000000_vp.bin
done
./plotvp ./output/model_$1 
mv temp ./output/model_$1/proc000000_vp.bin
xdg-open vp.png &
#sed -i "s:parameters =.*:parameters = ['rho']:g" ./plotbin
#./plotbin ./output/model_$1 testrho
#display testrho.png &
