# compute_zeros/zeta_zeros.py
# Author: Murphy
# Date: March 2025
# Description: Compute the first N non-trivial zeros of the Riemann zeta function and save them to a file.

from mpmath import zetazero
import os

# Path handling relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")

# Number of zeros to compute
N = 100

# Compute the first N non-trivial zeros
print(f"Computing the first {N} non-trivial zeros of the Riemann zeta function...")
zeros = [zetazero(k) for k in range(1, N + 1)]

# Create the results directory if it doesn't exist
os.makedirs(RESULTS_DIR, exist_ok=True)

# Save the zeros to a file
with open(os.path.join(RESULTS_DIR, "zeros_found.txt"), "w") as f:
    f.write("First {} non-trivial zeros of the Riemann zeta function:\n".format(N))
    for i, z in enumerate(zeros, 1):
        f.write(f"Zero {i}: s = {z}\n")

# Print the first 10 zeros for quick inspection
print("First 10 zeros:")
for i, z in enumerate(zeros[:10], 1):
    print(f"Zero {i}: s = {z}")

print(f"All {N} zeros have been saved to '{os.path.join('results', 'zeros_found.txt')}'.")
