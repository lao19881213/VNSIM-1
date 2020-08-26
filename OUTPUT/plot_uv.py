from matplotlib import pyplot as plt
import numpy as np 

data_uv = np.loadtxt('one_month.txt')
plt.figure()

ax = plt.gca()

plt.scatter(data_uv[:,0]/1000,data_uv[:,1]/1000, marker='.')

plt.xlabel('$u$($10^3\cdot$km)',fontsize=20)
plt.ylabel('$v$($10^3\cdot$km)',fontsize=20)

ax.tick_params(labelsize=18)

#plt.savefig('one_day.png')

plt.show() 
