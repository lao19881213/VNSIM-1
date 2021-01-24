from casatasks.private import simutil
import argparse


parser = argparse.ArgumentParser(description='radec2itrf')

parser.add_argument('--ra', dest='ra', type=float, default='43.82', help='RA of Antenna in deg')
parser.add_argument('--dec', dest='dec', type=float, default='87.57', help='DEC of Antenna in deg')
parser.add_argument('--at', dest='altitude', type=float, default='100', help='Altitude of Antenna in metre')


args = parser.parse_args()

ra = args.ra
dec = args.dec
altitude = args.altitude

u=simutil.simutil()
itrf_xyz = u.locxyz2itrf(ra,dec,altitude)
print(itrf_xyz)
