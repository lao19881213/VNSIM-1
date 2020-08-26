#!/bin/bash

for row_id in $(seq 21843 -1 11844)
do 
   echo $row_id
   python3 /home/lbq/work/VNSIM-1/creat_ini.py -i $row_id
   python3 Func_uv.py -c /home/lbq/work/VNSIM-1/CONFIG_FILE/config_uv_moon_test.ini -s /home/lbq/work/VNSIM-1/OUTPUT/moon_uv/uvdata_${row_id}.txt
done
