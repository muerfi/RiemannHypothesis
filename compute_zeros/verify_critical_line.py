# compute_zeros/verify_critical_line.py
# Author: Murphy
# Date: March 2025
# Description: Verify that the real parts of the computed non-trivial zeros are 1/2 and compare with known zeros.

import re
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Read the computed zeros from the file
computed_zeros = []
with open(os.path.join(RESULTS_DIR, "zeros_found.txt"), "r") as f:
    lines = f.readlines()
    for line in lines[1:]:  # Skip the header
        match = re.search(r"s = (.+?) \+ (.+?)j", line)
        if match:
            real_part = float(match.group(1))
            imag_part = float(match.group(2))
            computed_zeros.append(complex(real_part, imag_part))

# Verify that the real parts are 1/2
expected_real = 0.5
tolerance = 1e-10  # Numerical precision tolerance
all_on_critical_line = True
for z in computed_zeros:
    if abs(z.real - expected_real) > tolerance:
        print(f"Zero {z} is off the critical line! Real part: {z.real}")
        all_on_critical_line = False

if all_on_critical_line:
    print("All computed zeros lie on the critical line (Re(s) = 1/2) within tolerance.")
else:
    print("Some zeros do not lie on the critical line!")

# Compare with known zeros (first 10)
known_zeros = []
with open(os.path.join(DATA_DIR, "known_zeros.txt"), "r") as f:
    lines = f.readlines()
    for line in lines:
        match = re.search(r"s = (.+?) \+ (.+?)j", line)
        if match:
            real_part = float(match.group(1))
            imag_part = float(match.group(2))
            known_zeros.append(complex(real_part, imag_part))

# Compare the first 10 computed zeros with known zeros
print("\nComparing the first 10 computed zeros with known zeros:")
for i, (computed, known) in enumerate(zip(computed_zeros[:10], known_zeros), 1):
    diff = abs(computed - known)
    print(f"Zero {i}: Computed = {computed}, Known = {known}, Difference = {diff:.2e}")
    if diff > tolerance:
        print(f"Warning: Large discrepancy for zero {i}!")
      
