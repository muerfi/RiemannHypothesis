# prime_distribution/visualizations/prime_error_plot.py
# Author: Murphy
# Date: March 2025
# Description: Visualize the error between the exact π(x) and the Riemann approximation.

import numpy as np
import matplotlib.pyplot as plt

# Read the error data
data = np.loadtxt("error_data.txt", delimiter=",", skiprows=1)
x_values = data[:, 0]
exact_pi_x = data[:, 1]
approx_pi_x = data[:, 2]
absolute_errors = data[:, 3]
relative_errors = data[:, 4]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, absolute_errors, marker='o', linestyle='-', color='red', label='Absolute Error')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('x (log scale)')
plt.ylabel('Absolute Error (log scale)')
plt.title('Error in Riemann Approximation of π(x)')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
