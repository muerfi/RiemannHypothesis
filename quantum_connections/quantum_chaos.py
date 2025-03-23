# quantum_connections/quantum_chaos.py
# Author: Murphy
# Date: March 2025
# Description: Simulate the energy levels of a quantum chaotic system (stadium billiard).

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
import os

# Parameters for the stadium billiard (simplified as a perturbed rectangle)
L_x = 1.0  # Length of the rectangle (x-direction)
L_y = 1.0  # Width of the rectangle (y-direction)
perturbation = 0.1  # Perturbation to introduce chaos
N = 100  # Grid points in each direction (for discretization)

# Discretize the domain
x = np.linspace(0, L_x, N)
y = np.linspace(0, L_y, N)
dx = x[1] - x[0]
dy = y[1] - y[0]

# Create the Laplacian operator using finite differences
# Total number of points
N_total = N * N
# Indices for the grid points
indices = np.arange(N_total).reshape(N, N)

# Create the sparse Laplacian matrix
diagonals = np.zeros(N_total)
off_diagonals_x = np.zeros(N_total - 1)
off_diagonals_y = np.zeros(N_total - N)

# Fill the diagonals
for i in range(N):
    for j in range(N):
        idx = indices[i, j]
        diagonals[idx] = -2 / dx**2 - 2 / dy**2
        # Perturbation to simulate stadium-like chaos
        if i == N // 2 and j == N // 2:  # Perturb the center
            diagonals[idx] += perturbation
        # x-direction connections
        if j < N - 1:
            off_diagonals_x[idx] = 1 / dx**2
        # y-direction connections
        if i < N - 1:
            off_diagonals_y[idx] = 1 / dy**2

# Construct the sparse matrix
Laplacian = sparse.diags(
    [off_diagonals_y, off_diagonals_x, diagonals, off_diagonals_x, off_diagonals_y],
    [-N, -1, 0, 1, N],
    shape=(N_total, N_total)
)

# Solve for the eigenvalues (energy levels)
num_levels = 100  # Number of energy levels to compute
eigenvalues, _ = eigsh(-Laplacian, k=num_levels, which='SM')  # Smallest magnitude
energy_levels = np.sort(eigenvalues)

# Compute the spacings between consecutive energy levels
spacings = np.diff(energy_levels)

# Normalize the spacings (mean spacing = 1)
mean_spacing = np.mean(spacings)
normalized_spacings = spacings / mean_spacing

# Save the normalized spacings for comparison
os.makedirs("visualizations", exist_ok=True)
np.savetxt("visualizations/energy_spacings.txt", normalized_spacings)

print(f"Computed {num_levels} energy levels of the stadium billiard.")
print("First 10 energy levels:", energy_levels[:10])
print(f"Normalized spacings saved to 'visualizations/energy_spacings.txt'.")
