#!/bin/bash

RA_DEC="RA00DEC90 RA00DEC60 RA00DEC30 RA00DEC00"

START_TIME="2021/10/01/13/00/00"
STOP_TIME="2021/10/01/16/00/00"

hours=(3)

OBS_N_ALL="qitai_square qitai_circle qitai_t_shape qitai_y_shape qitai_spiral qitai_hybrid qitai_hybrid_46_p1 qitai_hybrid_46_p2"

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
	        python3 creat_ini_new.py -s $radec -t $START_TIME -p $stoptime -i config_uv_img_${OBS_N}.ini
	        python3 Func_img.py -c config_uv_img_${OBS_N}.ini -n ${OBS_N}_${radec}_${hours[$i]}h -i -f png	
        done
done
done
