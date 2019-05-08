import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

maxv = 100
ints = 1000

x = np.linspace(0,maxv, ints)
y = np.linspace(0,maxv, ints)
x, y = np.meshgrid(x,y)

z = np.divide(np.add(np.square(x),np.square(y)),np.add(np.multiply(x,y),1))

line = ax.plot_surface(x,y,z)
plt.show()