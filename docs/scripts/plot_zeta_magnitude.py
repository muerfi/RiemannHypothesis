# Description: Generate a heatmap of |ζ(s)| in the critical strip.

import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta
import os

# Define the range for the real and imaginary parts
sigma_range = np.linspace(0, 0.99, 100)  # Real part (0 to 0.99, avoiding the pole at σ=1)
t_range = np.linspace(0, 50, 200)        # Imaginary part (0 to 50)
sigma, t = np.meshgrid(sigma_range, t_range)

# Compute the magnitude of zeta(s)
z = np.zeros_like(sigma, dtype=float)
for i in range(len(t_range)):
    for j in range(len(sigma_range)):
        s = sigma[i, j] + 1j * t[i, j]
        z[i, j] = abs(zeta(s))

# Create the heatmap
plt.figure(figsize=(8, 6))
plt.imshow(z, extent=[0, 0.99, 0, 50], origin='lower', cmap='viridis', aspect='auto')
plt.colorbar(label='|ζ(σ + it)|')
plt.xlabel('Real Part (σ)')
plt.ylabel('Imaginary Part (t)')
plt.title('Magnitude of ζ(s) in the Critical Strip')

# Save the plot
os.makedirs("images", exist_ok=True)
plt.savefig("images/zeta_magnitude.png", dpi=300, bbox_inches='tight')
plt.close()