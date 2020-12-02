import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt('./DATABASE/kelamayi_square')
kelamayi = [422004.46595514845, 433656.1093357418, 6328482.528906228]#[316256.0608078195, 4419742.117422923, 4572958.2123400485]
plt.figure()
plt.plot(data[:,0]-kelamayi[0], data[:,1]-kelamayi[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.axis("equal")
plt.savefig('kelamayi_square.png')

data = np.loadtxt('./DATABASE/kelamayi_circle')
kelamayi = [422004.46595514845, 433656.1093357418, 6328482.528906228]#[316256.0608078195, 4419742.117422923, 4572958.2123400485]
plt.figure()
plt.plot(data[:,0]-kelamayi[0], data[:,1]-kelamayi[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.axis('equal')
plt.savefig('kelamayi_circle.png')

data = np.loadtxt('./DATABASE/kelamayi_t_shape')
kelamayi = [422004.46595514845, 433656.1093357418, 6328482.528906228]#[316256.0608078195, 4419742.117422923, 4572958.2123400485]
plt.figure()
plt.plot(data[:,0]-kelamayi[0], data[:,1]-kelamayi[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.axis('equal')
plt.savefig('kelamayi_t_shape.png')

data = np.loadtxt('./DATABASE/kelamayi_y_shape')
kelamayi = [422004.46595514845, 433656.1093357418, 6328482.528906228]#[316256.0608078195, 4419742.117422923, 4572958.2123400485]
plt.figure()
plt.plot(data[:,0]-kelamayi[0], data[:,1]-kelamayi[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.axis('equal')
plt.savefig('kelamayi_y_shape.png')

data = np.loadtxt('./DATABASE/kelamayi_spiral')
kelamayi = [422004.46595514845, 433656.1093357418, 6328482.528906228]#[316256.0608078195, 4419742.117422923, 4572958.2123400485]
plt.figure()
plt.plot(data[:,0]-kelamayi[0], data[:,1]-kelamayi[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.axis('equal')
plt.savefig('kelamayi_spiral.png')

#data = np.loadtxt('./DATABASE/kelamayi_hybrid')
#kelamayi = [316256.0608078195, 4419742.117422923, 4572958.2123400485]
#plt.figure()
#plt.plot(data[:,0]-kelamayi[0], data[:,1]-kelamayi[1],'b^')
#plt.xlabel('East(m)')
#plt.ylabel('North(m)')
#plt.axis('equal')
#plt.savefig('kelamayi_hybrid.png')

data = np.loadtxt('./DATABASE/kelamayi_hybrid_square')
kelamayi = [422004.46595514845, 433656.1093357418, 6328482.528906228]#[316256.0608078195, 4419742.117422923, 4572958.2123400485]
plt.figure()
plt.plot(data[:,0]-kelamayi[0], data[:,1]-kelamayi[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.axis('equal')
plt.savefig('kelamayi_hybrid_square.png')

#data = np.loadtxt('./DATABASE/kelamayi_hybrid_46_p2')
#kelamayi = [316256.0608078195, 4419742.117422923, 4572958.2123400485]
#plt.figure()
#plt.plot(data[:,0]-kelamayi[0], data[:,1]-kelamayi[1],'b^')
#plt.xlabel('East(m)')
#plt.ylabel('North(m)')
#plt.axis('equal')
#plt.savefig('kelamayi_hybrid_46_p2.png')

