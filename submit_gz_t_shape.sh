#!/bin/bash 

#SBATCH --partition=purley-cpu
##SBATCH --time=15:00:00
#SBATCH --job-name=vlbis
#SBATCH --nodes=1
#SBATCH --mem=60gb
#SBATCH --export=all
#SBATCH --nodelist=purley-x86-cpu05
#SBATCH --output=img_gz_t_shape.o
#SBATCH --error=img_gz_t_shape.e
export PATH=/home/blao/anaconda3/bin:$PATH

./run_gz_t_shape_img.sh
