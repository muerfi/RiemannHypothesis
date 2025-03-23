# prime_distribution/riemann_approx.py
# Author: Murphy
# Date: March 2025
# Description: Approximate π(x) using the Riemann explicit formula with non-trivial zeros.

import numpy as np
from mpmath import li
import re

# Read the non-trivial zeros from the file
zeros = []
with open("../compute_zeros/results/zeros_found.txt", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:  # Skip the header
        match = re.search(r"s = (.+?) \+ (.+?)j", line)
        if match:
            real_part = float(match.group(1))
            imag_part = float(match.group(2))
            zeros.append(complex(real_part, imag_part))

# Function to compute the Riemann approximation of π(x)
def riemann_approx(x, zeros):
    """Approximate π(x) using the Riemann explicit formula."""
    if x < 2:
        return 0
    # Main term: Li(x)
    main_term = float(li(x))
    # Correction for x^(1/2)
    correction = 0.5 * float(li(x**0.5))
    # Sum over non-trivial zeros
    sum_zeros = 0
    for rho in zeros:
        sum_zeros += float(li(x**rho))
        # Include the conjugate zero (since zeros come in conjugate pairs)
        sum_zeros += float(li(x**rho.conjugate()))
    return main_term - correction - sum_zeros

# Test the approximation for various values of x
x_values = [10**k for k in range(1, 7)]  # x = 10, 100, ..., 1000000
pi_x_approx = [riemann_approx(x, zeros) for x in x_values]

# Print results
print("Approximated π(x) using the Riemann explicit formula:")
for x, approx in zip(x_values, pi_x_approx):
    print(f"π({x}) ≈ {approx:.2f}")
  
