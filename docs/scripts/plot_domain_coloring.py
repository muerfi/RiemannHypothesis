# docs/plot_domain_coloring.py
# Author: Murphy
# Date: March 2025
# Description: Generate a domain coloring plot of ζ(s).

import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta
import os

# Define the range for the real and imaginary parts
sigma_range = np.linspace(-2, 2, 400)  # Real part
t_range = np.linspace(-30, 30, 600)    # Imaginary part
sigma, t = np.meshgrid(sigma_range, t_range)

# Compute zeta(s)
z = np.zeros_like(sigma, dtype=complex)
for i in range(len(t_range)):
    for j in range(len(sigma_range)):
        s = sigma[i, j] + 1j * t[i, j]
        z[i, j] = zeta(s)

# Compute the argument and magnitude
arg = np.angle(z)
mag = np.log(np.abs(z) + 1)

# Create an HSV color map
h = (arg + np.pi) / (2 * np.pi)
s = np.ones_like(h)
v = mag / (mag.max() + 1e-10)
hsv = np.dstack((h, s, v))
from matplotlib.colors import hsv_to_rgb
rgb = hsv_to_rgb(hsv)

# Create the plot
plt.figure(figsize=(8, 6))
plt.imshow(rgb, extent=[sigma_range[0], sigma_range[-1], t_range[0], t_range[-1]], origin='lower')
plt.xlabel('Real Part (σ)')
plt.ylabel('Imaginary Part (t)')
plt.title('Domain Coloring of ζ(s)')
plt.grid(False)

# Save the plot
os.makedirs("images", exist_ok=True)
plt.savefig("images/domain_coloring.png", dpi=300, bbox_inches='tight')
plt.close()