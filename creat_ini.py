import configparser
import numpy as np
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Run the vlbi-moon UV plots")
    parser.add_argument('-i',
                        '--row_id',
                        default='0',
                        help='Specify the row_id')

    return parser.parse_args()


args = parse_args()
row_id = int(args.row_id)

data_moon = np.loadtxt('xyz_EME2000_230601_230701',usecols =(0,1,2,3,4), dtype=int)
#print(data_moon.shape)
year = int(data_moon[row_id,0])

m = int(data_moon[row_id,1])

d = int(data_moon[row_id,2])

h = int(data_moon[row_id,3])

mi = int(data_moon[row_id,4])

str_start = '%s/%02d/%02d/%02d/%02d/00' % (year,m,d,h,mi)


if row_id == 43201:
   year_1 = 2023

   m_1 = 7

   d_1 = 1

   h_1 = 0

   mi_1 = 1
else:
   year_1 = int(data_moon[row_id+1,0])

   m_1 = int(data_moon[row_id+1,1])

   d_1 = int(data_moon[row_id+1,2])

   h_1 = int(data_moon[row_id+1,3])

   mi_1 = int(data_moon[row_id+1,4])

str_stop = '%s/%02d/%02d/%02d/%02d/00' % (year_1,m_1,d_1,h_1,mi_1)

conf = configparser.ConfigParser()

ini_file = '/home/lbq/work/VNSIM-1/CONFIG_FILE/config_uv_moon_test.ini'

conf.read(ini_file)

conf.set("obs_time", "start", str_start)

conf.set("obs_time", "end", str_stop)

str_vlbi = "Kunming, Tianma, Urumqi, MIYUN, moon_%s" % row_id 
conf.set("station", "pos_vlbi", str_vlbi)

fh = open(ini_file ,'w')

conf.write(fh)

fh.close()
