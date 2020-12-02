#!/bin/bash

RA_DEC="RA00DEC00 RA00DEC30 RA00DEC60 RA00DEC90"

START_TIME="2021/10/01/15/00/00"
STOP_TIME="2021/10/01/15/30/00"

hours=(0.5)

OBS_N_ALL="kelamayi_hybrid_square"

for OBS_N in $OBS_N_ALL;
do
echo ${OBS_N}	
for radec in $RA_DEC;
do
	echo $radec
	i=0
	for stoptime in $STOP_TIME;
	do
                echo ${hours[$i]}h	
	        python3 creat_ini_new.py -n ${OBS_N} -s $radec -t $START_TIME -p $stoptime -i config_uv_img_${OBS_N}.ini #-m "RadioGalaxy.model" 
	        python3 Func_img_array.py -c config_uv_img_${OBS_N}.ini -n ${OBS_N}_${radec}_${hours[$i]}h -i -f png	
        done
done
done
