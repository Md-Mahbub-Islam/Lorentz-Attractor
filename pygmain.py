import numpy as np
import pygame
import imageio

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

# Set up the Pygame display
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lorenz Attractor")
clock = pygame.time.Clock()

# Initialize the GIF writer
frames = []
filename = "lorenz_attractor.gif"

# Set up the colors and line width
color = (255, 255, 255)
linewidth = 1

# Set up the scaling factors and offsets
scale = 10
x_offset = height / 4
y_offset = width / 4

# Draw the Lorenz attractor
for i in range(len(soln)):
    x, y, z = soln[i] * scale
    x, z = z, y
    x += x_offset
    z += y_offset
    frames.append(pygame.surfarray.array3d(screen))
    if i == 0:
        pygame.draw.circle(screen, color, (int(x), int(z)), linewidth)
    else:
        pygame.draw.line(screen, color, (prev_x, prev_z), (x, z), linewidth)
    prev_x, prev_z = x, z
    pygame.display.update()
    clock.tick(60)

# Save the frames as a GIF
imageio.mimsave(filename, frames, fps=60)

pygame.quit()
