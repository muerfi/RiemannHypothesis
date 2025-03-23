# theoretical_approaches/de_bruijn_newman.py
# Author: Murphy
# Date: March 2025
# Description: Estimate the de Bruijn-Newman constant by analyzing the movement of zeros.

import numpy as np
from mpmath import xi, mp
import re

# Set precision for mpmath
mp.dps = 25  # Decimal places of precision

# Read the first 10 non-trivial zeros from the file
zeros = []
with open("../compute_zeros/results/zeros_found.txt", "r") as f:
    lines = f.readlines()
    for line in lines[1:11]:  # First 10 zeros
        match = re.search(r"s = (.+?) \+ (.+?)j", line)
        if match:
            real_part = float(match.group(1))
            imag_part = float(match.group(2))
            zeros.append(complex(real_part, imag_part))

# Simplified model: Approximate the movement of zeros as t changes
# We use the xi function and simulate the effect of t on the zeros
def approximate_zero_movement(t, s0, num_steps=100, step_size=0.01):
    """
    Approximate the movement of a zero s0 under the de Bruijn-Newman deformation.
    Returns the real part of the zero after applying the deformation.
    """
    s = complex(s0)
    for _ in range(num_steps):
        # Compute xi(s) and its derivative to approximate the zero's movement
        xi_val = xi(s)
        delta_s = step_size * (t * s.imag**2)  # Simplified perturbation
        s = s - delta_s * (xi_val / (xi(s + 1e-5) - xi_val))  # Newton-like step
    return s.real

# Test different values of t to find when zeros move off the critical line
t_values = np.linspace(-0.5, 0.5, 100)  # Range of t to test
critical_line = 0.5
tolerance = 1e-5

print("Estimating the de Bruijn-Newman constant...")
for t in t_values:
    all_on_critical_line = True
    for s0 in zeros:
        new_real = approximate_zero_movement(t, s0)
        if abs(new_real - critical_line) > tolerance:
            all_on_critical_line = False
            break
    if not all_on_critical_line:
        print(f"At t = {t:.3f}, some zeros move off the critical line.")
        print(f"Estimated de Bruijn-Newman constant Λ ≈ {t:.3f}")
        break
else:
    print("All zeros remained on the critical line for the tested t values.")
