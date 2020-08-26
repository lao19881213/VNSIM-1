#!/bin/bash
for row_id in $(seq 0 1 43201)
do

   cat ./moon_uv/uvdata_${row_id}.txt >> one_month.txt 

done
