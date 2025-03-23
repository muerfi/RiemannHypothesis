# quantum_connections/zeros_spacing.py
# Author: Murphy
# Date: March 2025
# Description: Compute the normalized spacings between consecutive non-trivial zeros.

import numpy as np
import re
import os

# Read the non-trivial zeros
zeros = []
with open("../compute_zeros/results/zeros_found.txt", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:  # Skip the header
        match = re.search(r"s = (.+?) \+ (.+?)j", line)
        if match:
            real_part = float(match.group(1))
            imag_part = float(match.group(2))
            zeros.append(complex(real_part, imag_part))

# Extract the imaginary parts
imag_parts = np.array([z.imag for z in zeros])

# Compute the spacings between consecutive zeros
spacings = np.diff(imag_parts)

# Normalize the spacings (mean spacing = 1)
mean_spacing = np.mean(spacings)
normalized_spacings = spacings / mean_spacing

# Save the normalized spacings for comparison
os.makedirs("visualizations", exist_ok=True)
np.savetxt("visualizations/zeros_spacings.txt", normalized_spacings)

print(f"Computed spacings for {len(imag_parts)} non-trivial zeros.")
print("First 10 spacings:", spacings[:10])
print(f"Normalized spacings saved to 'visualizations/zeros_spacings.txt'.")
