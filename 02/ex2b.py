import numpy as np 
import matplotlib.pyplot as plt 
from ex2a import diffdrive 

plt.gca().set_aspect('equal')

l = 0.5
x = 1.5
y = 2.0
theta = np.pi/2

plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("starting pose: x: %f, y: %f, theta: %f" % (x, y, theta))

#first motion
v_l = 0.3
v_r = 0.3
t = 3
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after motion 1: x: %f, y: %f, theta: %f" % (x, y, theta))

v_l = 0.1
v_r = -0.1
t = 1
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after motion 2: x: %f, y: %f, theta: %f" % (x, y, theta))

v_l = 0.2
v_r = 0
t = 2
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after motion 3: x: %f, y: %f, theta: %f" % (x, y, theta))

plt.xlim([0.5, 2.5])
plt.ylim([1.5, 3.5])

plt.show()