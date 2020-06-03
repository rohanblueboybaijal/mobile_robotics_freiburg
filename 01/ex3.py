import math 
import numpy as np 
import matplotlib.pyplot as plt 

pi = math.pi

scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-pi/2,pi/2, np.shape(scan)[0], endpoint='true')

x = scan*np.sin(angle)
y = scan*np.cos(angle)

# plt.plot(x,y,'.k', markersize=3)

# plt.gca().set_aspect('equal')
# #plt.show()

T_global_robot = np.array([[np.cos(pi/4), -np.sin(pi/4), 1.0],
               [np.sin(pi/4), np.cos(pi/4), 0.5],
               [0.0, 0.0, 1.0]] )

T_robot_laser = np.array([[np.cos(pi), -np.sin(pi), 0.2],
                         [np.sin(pi), np.cos(pi), 0.0],
                         [0.0, 0.0, 1.0]])


T_global_laser = T_global_robot @ T_robot_laser

w = np.ones(len(x))

scan_laser = np.array([x,y,w])
scan_global = np.dot(T_global_laser, scan_laser)

plt.figure()
plt.plot(scan_global[0,:], scan_global[1,:], '.k', markersize=3)

plt.plot(T_global_robot[0,2], T_global_robot[1,2], '+b')
plt.plot(T_global_laser[0,2], T_global_laser[1,2], '+r')

plt.gca().set_aspect('equal')
plt.show()
