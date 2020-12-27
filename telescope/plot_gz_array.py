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


