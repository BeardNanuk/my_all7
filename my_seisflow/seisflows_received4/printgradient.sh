#!/bin/bash


rm ./output/gradient_$1/proc*_x.bin
rm ./output/gradient_$1/proc*_z.bin
cp model_init80/proc0*_x.bin ./output/gradient_$1
cp model_init80/proc0*_z.bin ./output/gradient_$1
cp ./output/gradient_$1/proc000000_vp_kernel.bin temp
NPROC=9
for i in `seq 1 $NPROC`;
do
str='_x.bin'
cat ./output/gradient_$1/proc00000$i$str >> ./output/gradient_$1/proc000000_x.bin
str='_z.bin'
cat ./output/gradient_$1/proc00000$i$str >> ./output/gradient_$1/proc000000_z.bin
str='_vp_kernel.bin'
cat ./output/gradient_$1/proc00000$i$str >> ./output/gradient_$1/proc000000_vp_kernel.bin
done

./plotbin ./output/gradient_$1 vp_kernel 
mv temp ./output/gradient_$1/proc000000_vp_kernel.bin

display vp_kernel.png 
