#!/bin/bash

RA_DEC="RA00DEC90 RA00DEC60 RA00DEC30"

STOP_TIME="2021/10/01/01/00/00 2021/10/01/03/00/00 2021/10/01/06/00/00"

hours=(1 3 6)

OBS_N='qitai_y_shape_new'

for radec in $RA_DEC;
do
	echo $radec
	i=0
	for stoptime in $STOP_TIME;
	do
                		
	        python3 creat_ini_new.py -s $radec -p $stoptime -i config_uv_${OBS_N}.ini 
                python3 Func_uv.py -c config_uv_${OBS_N}.ini  -f png -n ${OBS_N}_${radec}_${hours[$i]}h
		let i+=1 
        done
done
