import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt('./DATABASE/qitai_square_new1')
qitai = [195430.71627589973, 4605201.947129761, 4393683.098043822]
plt.figure()
plt.plot(data[:,0]-qitai[0], data[:,1]-qitai[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.savefig('qitai_square.png')

data = np.loadtxt('./DATABASE/qitai_circle_new')
qitai = [195430.71627589973, 4605201.947129761, 4393683.098043822]
plt.figure()
plt.plot(data[:,0]-qitai[0], data[:,1]-qitai[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.axis('equal')
plt.savefig('qitai_circle.png')

data = np.loadtxt('./DATABASE/qitai_t_shape_new')
qitai = [195430.71627589973, 4605201.947129761, 4393683.098043822]
plt.figure()
plt.plot(data[:,0]-qitai[0], data[:,1]-qitai[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.savefig('qitai_t_shape.png')

data = np.loadtxt('./DATABASE/qitai_y_shape_new')
qitai = [195430.71627589973, 4605201.947129761, 4393683.098043822]
plt.figure()
plt.plot(data[:,0]-qitai[0], data[:,1]-qitai[1],'b^')
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.savefig('qitai_y_shape.png')
