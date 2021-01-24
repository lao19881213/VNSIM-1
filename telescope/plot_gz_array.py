import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt('gz_spiral.txt')
gz = [-1668.557207, 5506.838527,2744.934966]
plt.figure()
plt.plot(data[:,0]-gz[0], data[:,1]-gz[1],'b^')
plt.xlabel('East(km)')
plt.ylabel('North(km)')
plt.axis("equal")
plt.savefig('gz_spiral.png')

#others 4 locations
#[blao@x86-logon01 VNSIM-1]$ python3 radec2itrf.py --ra 107.08385555555554 --dec 28.52091111111111 --at 1391.01
#(-1651740.7116200358, -897602.7359445131, 6075829.232580593)
#[blao@x86-logon01 VNSIM-1]$ python3 radec2itrf.py --ra 108.32827222222222 --dec 28.58138333333333 --at 1097.91
#(-1766899.784731416, -962600.4029320397, 6033309.445597313)
#[blao@x86-logon01 VNSIM-1]$ python3 radec2itrf.py --ra 108.25675555555556 --dec 27.233922222222223 --at 1029.23
#(-1782290.0439541605, -917306.9898340167, 6035749.3328213245)
#[blao@x86-logon01 VNSIM-1]$ python3 radec2itrf.py --ra 104.7829295 --dec 24.870416527777778 --at 1576.596
#(-1481512.0576514273, -686765.4547585718, 6146516.744991903)

data = np.loadtxt('gz_spiral_1.txt')
gz = [-1651.7407116200358, -897.6027359445131, 6075.829232580593]
plt.figure()
plt.plot(data[:,0]-gz[0], data[:,1]-gz[1],'b^')
plt.xlabel('East(km)')
plt.ylabel('North(km)')
plt.title('ra=107.08 deg, dec=28.52 deg, alt=1391.01 m')
plt.axis("equal")
plt.savefig('gz_spiral_1.png')

data = np.loadtxt('gz_spiral_2.txt')
gz = [-1766.899784731416, -962.6004029320397, 6033.309445597313]
plt.figure()
plt.plot(data[:,0]-gz[0], data[:,1]-gz[1],'b^')
plt.xlabel('East(km)')
plt.ylabel('North(km)')
plt.title('ra=108.33 deg, dec=28.58 deg, alt=1097.91 m')
plt.axis("equal")
plt.savefig('gz_spiral_2.png')

data = np.loadtxt('gz_spiral_3.txt')
gz = [-1782.2900439541605, -917.3069898340167, 6035.7493328213245]
plt.figure()
plt.plot(data[:,0]-gz[0], data[:,1]-gz[1],'b^')
plt.xlabel('East(km)')
plt.ylabel('North(km)')
plt.title('ra=108.26 deg, dec=27.23 deg, alt=1029.23 m')
plt.axis("equal")
plt.savefig('gz_spiral_3.png')

data = np.loadtxt('gz_spiral_4.txt')
gz = [-1481.5120576514273, -686.7654547585718, 6146.516744991903]
plt.figure()
plt.plot(data[:,0]-gz[0], data[:,1]-gz[1],'b^')
plt.xlabel('East(km)')
plt.ylabel('North(km)')
plt.title('ra=104.78 deg, dec=24.87 deg, alt=1576.60 m')
plt.axis("equal")
plt.savefig('gz_spiral_4.png')

data = np.loadtxt('gz_t_shape.txt')
gz = [-1668.557207, 5506.838527,2744.934966]
plt.figure()
plt.plot(data[:,0]-gz[0], data[:,1]-gz[1],'b^')
plt.xlabel('East(km)')
plt.ylabel('North(km)')
plt.axis("equal")
plt.savefig('gz_t_shape.png')


