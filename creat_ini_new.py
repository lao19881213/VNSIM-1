import configparser
import numpy as np
import argparse

#[obs_time]
#start = 2021/10/01/00/00/00
#end = 2021/10/01/01/00/00
#step = 00/00/00/01
#
#[bs_type]
#bs_flag_gg = 1
#bs_flag_gs = 0
#bs_flag_ss = 0
#
#[obs_mode]
#obs_freq = 1.4e9
#bandwidth = 0.02e6
#cutoff_angle = 10.0
#precession_mode = 0
#unit_flag = km
#
#[station]
#pos_source = RA00DEC30
#pos_vlbi = qitai_square_1, qitai_square_2, qitai_square_3, qitai_square_4, qitai_square_5, qitai_square_6, qitai_square_7, qitai_square_8, qitai_square_9, qitai_square_10, qitai_square_11, qitai_square_12, qitai_square_13, qitai_square_14, qitai_square_15, qitai_square_16
#pos_telemetry =
#pos_satellite =

def parse_args():
    parser = argparse.ArgumentParser(description="creat ini file")
    parser.add_argument('-t',
                        '--start_time',
                        default='2021/10/01/13/00/00',
                        help='Specify the obs start time')
    parser.add_argument('-p',
                        '--stop_time',
                        default='2021/10/01/16/00/00',
                        help='Specify the obs start time')
    parser.add_argument('-s',
                        '--source_pos',
                        default='RA00DEC90',
                        help='Specify the source position')

    parser.add_argument('-m',
                        '--source_model',
                        default='Point-source.model',
                        help='Specify the source model')

    parser.add_argument('-i',
                       '--conf_ini',
                       default='config_uv_qitai_square.ini',
                       help='Specify the ini conf file')

    return parser.parse_args()


args = parse_args()

str_start = args.start_time
str_stop = args.stop_time



conf = configparser.ConfigParser()

ini_file = './CONFIG_FILE/%s' % args.conf_ini

conf.read(ini_file)

conf.set("obs_time", "start", str_start)

conf.set("obs_time", "end", str_stop)

str_source_pos = args.source_pos
conf.set("station", "pos_source", str_source_pos)

str_source_model = args.source_model
conf.set("imaging", "source_model", str_source_model)
fh = open(ini_file ,'w')

conf.write(fh)

fh.close()
