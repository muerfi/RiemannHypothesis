# visualizations/zeros_plot.py
# Author: Murphy
# Date: March 2025
# Description: Plot of the first few non-trivial zeros of the Riemann zeta function on the critical line.

import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero

# Compute the first 10 non-trivial zeros
n_zeros = 10
zeros = [zetazero(k) for k in range(1, n_zeros + 1)]
imag_parts = [float(z.imag) for z in zeros]

# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter([0.5] * n_zeros, imag_parts, color='red', label='Non-trivial Zeros')
plt.axvline(x=0.5, color='blue', linestyle='--', label='Critical Line (Re(s) = 1/2)')
plt.xlabel('Real Part (Re(s))')
plt.ylabel('Imaginary Part (Im(s))')
plt.title('First 10 Non-trivial Zeros of ζ(s) on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()

# Print the zeros
print("First 10 non-trivial zeros (Re(s) = 1/2):")
for i, z in enumerate(zeros, 1):
    print(f"Zero {i}: s = {z}")
  
