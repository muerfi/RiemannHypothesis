# visualizations/zeta_function_3d.py
# Author: Murphy
# Date: March 2025
# Description: 3D visualization of the magnitude of the Riemann zeta function in the critical strip.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpmath import zeta

# Define the range for the real and imaginary parts
sigma_range = np.linspace(0, 1, 100)  # Real part (0 to 1, critical strip)
t_range = np.linspace(0, 50, 200)     # Imaginary part (0 to 50)
sigma, t = np.meshgrid(sigma_range, t_range)

# Compute the magnitude of zeta(s) for s = sigma + it
z = np.zeros_like(sigma, dtype=float)
for i in range(len(t_range)):
    for j in range(len(sigma_range)):
        s = sigma[i, j] + 1j * t[i, j]
        z[i, j] = abs(zeta(s))

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(sigma, t, z, cmap='viridis')

# Add labels and title
ax.set_xlabel('Real Part (σ)')
ax.set_ylabel('Imaginary Part (t)')
ax.set_zlabel('|ζ(σ + it)|')
ax.set_title('3D Plot of |ζ(s)| in the Critical Strip')

# Add a color bar
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

# Show the plot
plt.show()
