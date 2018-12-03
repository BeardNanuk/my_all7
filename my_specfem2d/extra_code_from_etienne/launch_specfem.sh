#!/bin/sh


rm mesherz solverz 
rm -rf OUTPUT_FILES/*
/home/jiazeh/specfem2d/bin/xmeshfem2D >> mesherz

NPROC=1

mpirun -n $NPROC /home/jiazeh/specfem2d/bin/xspecfem2D >> solverz



