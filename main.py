import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lorenz attractor equations
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# Set up the initial conditions
x0, y0, z0 = (0.1, 0.0, 0.0)
dt = 0.01
t = np.arange(0, 100, dt)

# Initialize the solution array
soln = np.empty((len(t), 3))
soln[0] = np.array([x0, y0, z0])

# Solve the differential equation
for i in range(len(t) - 1):
    x_dot, y_dot, z_dot = lorenz(*soln[i])
    soln[i+1] = soln[i] + np.array([x_dot, y_dot, z_dot]) * dt

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim((-25, 25))
ax.set_ylim((-35, 35))
ax.set_zlim((5, 55))
ax.set_axis_off()

# Animate the plot
for i in range(len(soln)):
    ax.scatter(soln[i, 0], soln[i, 1], soln[i, 2], c='r', marker='o')
    plt.pause(0.001)

plt.show()
