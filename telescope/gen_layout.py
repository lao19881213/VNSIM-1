#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
generate the layout for telescope array.
Written by Shaoguang Guo
Modified by Baoqiang Lao
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_layout(telescope_number = 4, layout_type = 'square', telesccope_diameter = 10, telescope_space = 20, cite_locate = (0,0,0),outputfile='layout.txt'):
    '''
    telescope_number : how many telescopes
    layout_type : square, circle, t-shape,y-shape, spiral
    telescope_diameter: the diameter of telescope
    cite locate : x,y,z
    outputfile : the output of layout
    '''

    # get the coordinate, the left-bottom point
    x,y,z = cite_locate

    f = open(outputfile,'w')

    if layout_type == 'square':
        for i in range(int(np.sqrt(telescope_number)) + 1):
            for j in range(int(np.sqrt(telescope_number)) + 1):
                f.write(('{:.5f}, {:.5f}, {:.5f} \n').format(float(x + i*telescope_space ), float(y + j*telescope_space),  float(z)))
        f.close()
    elif layout_type == 'circle':
        for i in range(telescope_number):
            f.write(('{:.5f}, {:.5f}, {:.5f} \n').format((x + telescope_space*np.cos(2 * np.pi * i/telescope_number)),(y+ telescope_space * np.sin(2 *np.pi * i/telescope_number)),  float(z)))
        f.close()
    elif layout_type == 't-shape':
        ## 16 antennas
        # row = 8
        # col = 8
        ## 46 antennas
        #row = 23
        #col = 23
        # 200 antennas
        row = 100
        col = 100
        for i in range(row):
          f.write(('{:.5f}, {:.5f}, {:.5f} \n').format(float(x + i*telescope_space - telescope_space * row /2), float(y),  float(z)))
        for i in range(col):
          f.write(('{:.5f}, {:.5f}, {:.5f} \n').format(float(x), float(y + i*telescope_space),  float(z)))
        f.close()
    elif layout_type == 'y-shape':
        ## 16 antennas
        # row = 8
        # col = 8
        ## 46 antennas
        #row = 30
        #col = 16 # The middle line
        # 200 antennas
        row = 100
        col = 100 # The middle line
        ang = np.pi / 3 # 60 degree
        for i in range(row):
            xx = x
            if i >= row/2:
                yy = y +  (col + i- row/2)* telescope_space
                xx = x + (i-row/2)*telescope_space
            else:
                yy = y + (col + row/2 - i) * telescope_space
                xx  = xx - (row/2 - i) * telescope_space
            #print(yy)
            #f.write(('{:.5f}, {:.5f}, {:.5f} \n').format(float(x + i*telescope_space - telescope_space * row /2), float(y +  ),  float(z)))
            f.write(('{:.5f}, {:.5f}, {:.5f} \n').format(float(xx), float(yy),  float(z)))
        for i in range(col):
            f.write(('{:.5f}, {:.5f}, {:.5f} \n').format(float(x), float(y + i*telescope_space),  float(z)))
        f.close()
    elif layout_type == 'spiral':
        xx, yy, zz = xyz
        theta = np.radians(np.linspace(0, 120, int(telescope_number/3)))
        r = 5 * theta ** 2
        x = 10 * r * np.cos(theta) + xx #40 -> 20
        print(x)
        y = 10 * r * np.sin(theta) + yy #40 -> 10
        for i, v in enumerate(x):
            #print(i, ':', v, y[i])
            f.write(('{:.5f} {:.5f} {:.5f} \n').format((v), (y[i]), float(zz)))
        plt.plot(x, y)
        #print(x, y)
        theta = np.radians(np.linspace(0, 120, int(telescope_number/3)))
        r = 5 * theta ** 2
        x = 10 * r * np.cos(theta + 2 * np.pi / 3.0) + xx #40 -> 10
        y = 10 * r * np.sin(theta + 2 * np.pi / 3.0) + yy #40 -> 10
        for i, v in enumerate(x):
            #print(i, ':', v, y[i])
            f.write(('{:.5f} {:.5f} {:.5f} \n').format((v), (y[i]), float(zz)))
        plt.plot(x, y)
        #print(x, y)
        theta = np.radians(np.linspace(0, 120, int(telescope_number/3)))
        r = 5 * theta ** 2
        x = 10 * r * np.cos(theta + 2 * np.pi * 2 / 3.0) + xx # 40 -> 10
        y = 10 * r * np.sin(theta + 2 * np.pi * 2 / 3.0) + yy # 40 -> 10
        for i, v in enumerate(x):
            #print(i, ':', v, y[i])
            f.write(('{:.5f} {:.5f} {:.5f} \n').format((v), (y[i]), float(zz)))
        plt.plot(x, y)
        #print(x, y)
        print("remove the duplicate positions for spiral (the first line)")
        f.close()
    else:
        print('Now supported layout')

def get_spiral_loc(location,output='layout.txt',debug=False):
    pass

def get_hybrid_loc():
    # reference point
    xx,yy,zz = 316256.0608078195, 4419742.117422923, 4572958.2123400485 #195350.88017, 4606739.72910, 4394642.77560
    angle_every_point = np.pi / 12
    for i in range(5):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = i * angle_every_point
        x,y = xx + r*np.cos(angle), yy + r*np.sin(angle);
        print(x,',',y, ',  4394642.77560')
    for i in range(5):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = 2 * np.pi/3 + i *angle_every_point
        x,y = xx - np.abs(r*np.cos(angle)), yy + np.abs(r*np.sin(angle));
        print(x,',',y, ',  4394642.77560')
    for i in range(5):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = 4 * np.pi/3 + i * angle_every_point
        if angle < 3*np.pi / 2 :
            x,y = xx - np.abs(r*np.cos(angle)), yy - np.abs( r*np.sin(angle));
        else:
            x,y = xx + np.abs(r*np.cos(angle)), yy - np.abs( r*np.sin(angle));
        print(x,',',y, ',  4394642.77560')

def get_hybrid_loc_46():
    # reference point
    ## Kelamayi
    xx,yy,zz = 316256.06081, 4419742.11742, 4572958.21234
    ## QiTai
    ## xx,yy,zz = 195350.88017, 4606739.72910, 4394642.77560
    angle_every_point = np.pi / 20
    ext_no = 7
    ## Core
    for i in range(ext_no):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = i * angle_every_point
        if np.sin(angle) < 0:
            x,y = xx + r*np.cos(angle), yy - (r*np.sin(angle));
        else:
            x,y = xx + r*np.cos(angle), yy + (r*np.sin(angle));
        print(x,',',y, ',  4572958.21234')
    ## Ext
    for i in range(ext_no):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = 2 * np.pi/3 + i *angle_every_point
        if np.cos(angle) < 0:
            x,y = xx - np.abs(r*np.cos(angle)), yy + np.abs(r*np.sin(angle))
        else:
            x,y = xx + np.abs(r*np.cos(angle)), yy + np.abs(r*np.sin(angle))
        print(x,',',y, ',  4572958.21234')
    for i in range(ext_no):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = 4 * np.pi/3 + i * angle_every_point
        if angle < 3*np.pi / 2 :
            x,y = xx - np.abs(r*np.cos(angle)), yy - np.abs( r*np.sin(angle));
        else:
            x,y = xx + np.abs(r*np.cos(angle)), yy - np.abs( r*np.sin(angle));
        print(x,',',y, ',  4572958.21234')

def get_hybrid_loc_200(telescope_space = 40):
    f = open('kelamayi_hybrid_200.txt','w')
    # reference point
    ## Kelamayi
    xx,yy,zz = 422004.46595514845, 433656.1093357418, 6328482.528906228
    angle_every_point = np.pi / 100

    ## Core
    core_no = 144
    for i in range(int(np.sqrt(core_no))):
        for j in range(int(np.sqrt(core_no))):
            f.write(('{:.5f}, {:.5f}, {:.5f} \n').format(float(xx + (i - np.sqrt(core_no)/2) * telescope_space ), float(yy + (j - np.sqrt(core_no)/2) * telescope_space),
                                                         float(zz)))
    ext_no = 23
    ## Ext
    for i in range(ext_no):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = i * angle_every_point
        if np.sin(angle) < 0:
            x,y = xx + r*np.cos(angle), yy - (r*np.sin(angle));
        else:
            x,y = xx + r*np.cos(angle), yy + (r*np.sin(angle));
        print(x,',',y, ',  6328482.528906228')
        if x > xx + (np.sqrt(core_no)/2) * telescope_space or x < xx - (np.sqrt(core_no)/2) * telescope_space :
            f.write(('{:.5f}, {:.5f}, 6328482.528906228 \n').format((x), (y)))
    for i in range(ext_no):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = 2 * np.pi/3 + i *angle_every_point
        if np.cos(angle) < 0:
            x,y = xx - np.abs(r*np.cos(angle)), yy + np.abs(r*np.sin(angle))
        else:
            x,y = xx + np.abs(r*np.cos(angle)), yy + np.abs(r*np.sin(angle))
        print(x,',',y, ',  6328482.528906228')
        if x > xx + (np.sqrt(core_no)/2) * telescope_space or x < xx - (np.sqrt(core_no)/2) * telescope_space :
            f.write(('{:.5f}, {:.5f}, 6328482.528906228 \n').format((x), (y)))
    for i in range(ext_no):
        if i == 0:
            r = 100
        else:
            r = 200 * i
        angle = 4 * np.pi/3 + i * angle_every_point
        if angle < 3*np.pi / 2 :
            x,y = xx - np.abs(r*np.cos(angle)), yy - np.abs( r*np.sin(angle));
        else:
            x,y = xx + np.abs(r*np.cos(angle)), yy - np.abs( r*np.sin(angle));
        print(x,',',y, ',  6328482.528906228')
        if x > xx + (np.sqrt(core_no)/2) * telescope_space or x < xx - (np.sqrt(core_no)/2) * telescope_space :
            f.write(('{:.5f}, {:.5f}, 6328482.528906228 \n').format((x), (y)))



# gz
xyz = (-1668.557207, 5506.838527, 2744.934966) #in km


telescope_cnt = 36

generate_layout(telescope_number=telescope_cnt,layout_type='spiral', telesccope_diameter=4.5, cite_locate=xyz, outputfile='gz_spiral.txt')
