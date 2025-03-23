# quantum_connections/visualizations/spacing_comparison.py
# Author: Murphy
# Date: March 2025
# Description: Compare the spacing distributions of zeta zeros and quantum energy levels.

import numpy as np
import matplotlib.pyplot as plt

# Load the normalized spacings
zeros_spacings = np.loadtxt("../visualizations/zeros_spacings.txt")
energy_spacings = np.loadtxt("../visualizations/energy_spacings.txt")

# Create histograms
plt.figure(figsize=(10, 6))
plt.hist(zeros_spacings, bins=20, alpha=0.5, label='Zeta Zeros Spacings', density=True)
plt.hist(energy_spacings, bins=20, alpha=0.5, label='Energy Level Spacings', density=True)
plt.xlabel('Normalized Spacing')
plt.ylabel('Density')
plt.title('Spacing Distribution: Zeta Zeros vs Quantum Chaotic System')
plt.legend()
plt.grid(True)
plt.show()
