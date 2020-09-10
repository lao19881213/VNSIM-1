#!/bin/bash

RA_DEC="RA00DEC90 RA00DEC60 RA00DEC30"

STOP_TIME="2021/10/01/01/00/00 2021/10/01/03/00/00 2021/10/01/06/00/00"

hours=(1 3 6)

OBS_N_ALL="qitai_square qitai_circle qitai_t_shape qitai_y_shape qitai_spiral"

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
	        python3 creat_ini_new.py -s $radec -p $stoptime -i config_uv_img_${OBS_N}.ini
	        python3 Func_img.py -c config_uv_img_${OBS_N}.ini -n ${OBS_N}_${radec}_${hours[$i]}h -i -f png	
		let i+=1 
        done
done
done