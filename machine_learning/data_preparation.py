# machine_learning/data_preparation.py
# Author: Murphy
# Date: March 2025
# Description: Prepare the non-trivial zeros data for machine learning.

import numpy as np
import re
from sklearn.preprocessing import MinMaxScaler
import os

# Read the non-trivial zeros
zeros = []
with open("../compute_zeros/results/zeros_found.txt", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:  # Skip the header
        match = re.search(r"s = (.+?) \+ (.+?)j", line)
        if match:
            real_part = float(match.group(1))
            imag_part = float(match.group(2))
            zeros.append(complex(real_part, imag_part))

# Extract the imaginary parts
imag_parts = np.array([z.imag for z in zeros])

# Normalize the data
scaler = MinMaxScaler()
imag_parts_normalized = scaler.fit_transform(imag_parts.reshape(-1, 1)).flatten()

# Create sequences for LSTM (e.g., use the past 5 zeros to predict the next one)
sequence_length = 5
X, y = [], []
for i in range(len(imag_parts_normalized) - sequence_length):
    X.append(imag_parts_normalized[i:i + sequence_length])
    y.append(imag_parts_normalized[i + sequence_length])
X = np.array(X)
y = np.array(y)

# Reshape X for LSTM [samples, time steps, features]
X = X.reshape(X.shape[0], X.shape[1], 1)

# Save the data
os.makedirs("data", exist_ok=True)
np.save("data/X.npy", X)
np.save("data/y.npy", y)
np.save("data/imag_parts.npy", imag_parts)
np.save("data/scaler.npy", scaler)

print(f"Prepared {len(X)} sequences for training.")
print(f"Data saved to 'data/' directory.")
