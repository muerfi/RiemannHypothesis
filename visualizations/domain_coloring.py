# visualizations/domain_coloring.py
# Author: Murphy
# Date: March 2025
# Description: Domain coloring plot of the Riemann zeta function in the complex plane.

import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta

# Define the range for the real and imaginary parts
sigma_range = np.linspace(-2, 2, 400)  # Real part
t_range = np.linspace(-30, 30, 600)    # Imaginary part
sigma, t = np.meshgrid(sigma_range, t_range)

# Compute zeta(s) for s = sigma + it
z = np.zeros_like(sigma, dtype=complex)
for i in range(len(t_range)):
    for j in range(len(sigma_range)):
        s = sigma[i, j] + 1j * t[i, j]
        z[i, j] = zeta(s)

# Compute the argument (phase) and magnitude
arg = np.angle(z)  # Phase in [-pi, pi]
mag = np.log(np.abs(z) + 1)  # Log magnitude for better contrast

# Create an HSV color map: hue from argument, value from magnitude
h = (arg + np.pi) / (2 * np.pi)  # Normalize to [0, 1]
s = np.ones_like(h)  # Saturation = 1
v = mag / (mag.max() + 1e-10)  # Normalize magnitude to [0, 1]

# Convert HSV to RGB
hsv = np.dstack((h, s, v))
from matplotlib.colors import hsv_to_rgb
rgb = hsv_to_rgb(hsv)

# Create the plot
plt.figure(figsize=(10, 8))
plt.imshow(rgb, extent=[sigma_range[0], sigma_range[-1], t_range[0], t_range[-1]], origin='lower')
plt.xlabel('Real Part (σ)')
plt.ylabel('Imaginary Part (t)')
plt.title('Domain Coloring of ζ(s)')
plt.grid(False)
plt.show()
