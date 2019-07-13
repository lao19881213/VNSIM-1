import numpy as np
# LLA2ECEF - convert latitude, longitude, and altitude to
# earth-centered, earth-fixed (ECEF) cartesian
# 
# USAGE:
# x,y,z = lla2ecef(lat,lon,alt)
# 
# x = ECEF X-coordinate (m)
# y = ECEF Y-coordinate (m)
# z = ECEF Z-coordinate (m)
# lat = geodetic latitude (deg)
# lon = longitude (deg)
# alt = height above WGS84 ellipsoid (m)
# 
# Notes: This function assumes the WGS84 model.
# Latitude is customary geodetic (not geocentric).
# 
# Source: "Department of Defense World Geodetic System 1984"
# Page 4-4
# National Imagery and Mapping Agency
# Last updated June, 2004
# NIMA TR8350.2
# 
# Michael Kleder, July 2005
def lla2ecef(lat,lon,alt):
    lat,lon = np.deg2rad(lat), np.deg2rad(lon)
# WGS84 ellipsoid constants:
    a = 6378137
    e = 8.1819190842622e-2
# intermediate calculation
# (prime vertical radius of curvature)
    N = a / np.sqrt(1 - e**2 * np.sin(lat)**2)
# results:
    x = (N+alt) * np.cos(lat) * np.cos(lon)
    y = (N+alt) * np.cos(lat) * np.sin(lon)
    z = ((1-e**2) * N + alt) * np.sin(lat)
    return x,y,z

#test
#chanbaishan
lat = 41.783
lon = 127.733
alt = 300
x1,y1,z1 = lla2ecef(lat,lon,alt)

print(x1,y1,z1)
#jilin
lat = 43.817
lon = 126.333
alt = 300
x2,y2,z2 = lla2ecef(lat,lon,alt)
print(x2,y2,z2)

#hulunbeier
lat = 48.883
lon = 119.133
alt = 300
x3,y3,z3 = lla2ecef(lat,lon,alt)
print(x3,y3,z3)
