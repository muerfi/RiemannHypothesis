import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero
import os

# Ensure the images directory exists
if not os.path.exists("images"):
    os.makedirs("images")

# Compute the first 1000 non-trivial zeros
N = 1000
print("Computing the first 1000 non-trivial zeros...")
zeros = [float(zetazero(k).imag) for k in range(1, N+1)]

# Compute the normalized spacings
spacings = []
for n in range(N-1):
    gamma_n = zeros[n]
    gamma_np1 = zeros[n+1]
    # Average spacing at height gamma_n
    avg_spacing = (2 * np.pi) / np.log(gamma_n / (2 * np.pi))
    s = (gamma_np1 - gamma_n) / avg_spacing
    spacings.append(s)

# Compute the histogram of spacings
bins = np.linspace(0, 5, 50)
hist, bin_edges = np.histogram(spacings, bins=bins, density=True)

# Compute the GUE prediction
s = np.linspace(0, 5, 100)
gue = 1 - (np.sin(np.pi * s) / (np.pi * s))**2

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(s, gue, label="GUE Prediction", color="blue", linewidth=2)
plt.hist(spacings, bins=bins, density=True, alpha=0.5, label="Riemann Zeros", color="orange")
plt.xlabel("Normalized Spacing (s)", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.title("Pair Correlation of the First 1000 Riemann Zeros", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("images/pair_correlation.png", dpi=300, bbox_inches="tight")
plt.show()
print("Image saved as images/pair_correlation.png")