# prime_distribution/error_analysis.py
# Author: Murphy
# Date: March 2025
# Description: Compute the error between the exact π(x) and the Riemann approximation.

import numpy as np
from prime_count import sieve_of_eratosthenes
from riemann_approx import riemann_approx, zeros
import os

# Compute exact and approximated π(x) for various x
x_values = [10**k for k in range(1, 7)]  # x = 10, 100, ..., 1000000
exact_pi_x = [sieve_of_eratosthenes(x) for x in x_values]
approx_pi_x = [riemann_approx(x, zeros) for x in x_values]

# Compute the absolute and relative errors
absolute_errors = [abs(exact - approx) for exact, approx in zip(exact_pi_x, approx_pi_x)]
relative_errors = [abs(exact - approx) / exact for exact, approx in zip(exact_pi_x, approx_pi_x)]

# Print results
print("Error analysis between exact and approximated π(x):")
print("x\tExact π(x)\tApprox π(x)\tAbsolute Error\tRelative Error")
for x, exact, approx, abs_err, rel_err in zip(x_values, exact_pi_x, approx_pi_x, absolute_errors, relative_errors):
    print(f"{x}\t{exact}\t\t{approx:.2f}\t\t{abs_err:.2f}\t\t{rel_err:.4f}")

# Save the results for visualization
os.makedirs("visualizations", exist_ok=True)
with open("visualizations/error_data.txt", "w") as f:
    f.write("x,Exact,Approx,Absolute_Error,Relative_Error\n")
    for x, exact, approx, abs_err, rel_err in zip(x_values, exact_pi_x, approx_pi_x, absolute_errors, relative_errors):
        f.write(f"{x},{exact},{approx},{abs_err},{rel_err}\n")
