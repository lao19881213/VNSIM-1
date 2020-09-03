#!/bin/bash

RA_DEC="RA00DEC90 RA00DEC60 RA00DEC30"

STOP_TIME="2021/10/01/01/00/00 2021/10/01/03/00/00 2021/10/01/06/00/00"

hours=(1 3 6)

for radec in $RA_DEC;
do
	echo $radec
	i=0
	for stoptime in $STOP_TIME;
	do
		
	        python3 creat_ini_new.py -s $radec -p $stoptime 
                python3 Func_uv.py -c config_uv_qitai_square.ini  -f png -n qitai_square_${radec}_${hours[$i]}h
		let i+=1 
        done
done
