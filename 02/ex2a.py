import numpy as np 

def diffdrive(x, y, theta, v_l, v_r, t, l):

    if(v_l==v_r):
        v = v_l
        theta_n = theta
        x_n = x + v*np.cos(theta_n)*t
        y_n = y + v*np.sin(theta_n)*t

    else :
        R = (l/2.0)*(v_r + v_l)/(v_r - v_l)
        W = (v_r - v_l)/l
        ICC_x = x - R*np.sin(theta)
        ICC_y = y + R*np.cos(theta)

        dtheta = W*t

        T = np.array([[np.cos(dtheta), -np.sin(dtheta), 0],
                      [np.sin(dtheta), np.cos(dtheta), 0],
                      [0.0, 0.0, 1.0]])
        x_ICC = np.array([[x - ICC_x],
                         [y - ICC_y],
                         [theta]])
        
        t = np.array([[ICC_x],
                      [ ICC_y ],
                      [dtheta]])

        x_prime = np.matmul(T, x_ICC) + t
        x_n = x_prime[0][0]
        y_n = x_prime[1][0]
        theta_n = x_prime[2][0]
    
    return x_n, y_n, theta_n


