#!/bin/bash 

#SBATCH --partition=purley-cpu
##SBATCH --time=15:00:00
#SBATCH --job-name=vlbis
#SBATCH --nodes=1
#SBATCH --mem=60gb
#SBATCH --export=all
#SBATCH --nodelist=purley-x86-cpu05
#SBATCH --output=img_extend.o
#SBATCH --error=img_extend.e
export PATH=/home/blao/anaconda3/bin:$PATH

./run_kelamayi_img_e.sh
