import numpy as np 
import  matplotlib.pyplot as plt  

def log_inverse_sensor_model(z,c):
    # z-10 accounts for the starting positions according to resolution of grid
    if c>=z-10:
        return np.log(0.6/(1-0.6))
    else:
        return np.log(0.3/(1-0.3))


c = range(0,201,10)
# Starting position for every cell in cm

logodds = np.zeros(len(c))

meas = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]

prior = np.log(0.5/(1-0.5))

for i in range(len(meas)):
    for j in range(len(c)):
        if c[j] > meas[i] + 20:
            continue

        logodds[j] = logodds[j] + log_inverse_sensor_model(meas[i], c[j]) - prior

m = 1 - 1/(1 + np.exp(logodds))

plt.plot(c,m)
plt.xlabel('x-position (cm)')
plt.ylabel('occupancy p(x)')
#plt.savefig('graph.pdf')
plt.show()
