#!/bin/bash 

#SBATCH --partition=purley-cpu
##SBATCH --time=15:00:00
#SBATCH --job-name=vlbis
#SBATCH --nodes=1
#SBATCH --mem=60gb
#SBATCH --export=all
#SBATCH --nodelist=purley-x86-cpu05
#SBATCH --output=img_gz.o
#SBATCH --error=img_gz.e
export PATH=/home/blao/anaconda3/bin:$PATH

./run_gz_img.sh
