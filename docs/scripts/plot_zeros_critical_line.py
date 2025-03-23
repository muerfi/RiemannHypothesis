# Description: Plot the first 10 non-trivial zeros on the critical line.

import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero
import os

# Compute the first 10 non-trivial zeros
n_zeros = 10
zeros = [zetazero(k) for k in range(1, n_zeros + 1)]
imag_parts = [float(z.imag) for z in zeros]

# Create the plot
plt.figure(figsize=(6, 8))
plt.scatter([0.5] * n_zeros, imag_parts, color='red', label='Non-trivial Zeros')
plt.axvline(x=0.5, color='blue', linestyle='--', label='Critical Line (Re(s) = 1/2)')
plt.xlabel('Real Part (Re(s))')
plt.ylabel('Imaginary Part (Im(s))')
plt.title('First 10 Non-trivial Zeros of ζ(s)')
plt.legend()
plt.grid(True)

# Save the plot
os.makedirs("images", exist_ok=True)
plt.savefig("images/zeros_critical_line.png", dpi=300, bbox_inches='tight')
plt.close()