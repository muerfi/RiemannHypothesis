# machine_learning/data_preparation.py
# Author: Murphy
# Date: March 2025
# Description: Prepare the non-trivial zeros data for machine learning.

import numpy as np
import re
from sklearn.preprocessing import MinMaxScaler
import os
import pickle

# Base directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read the non-trivial zeros
zeros = []
zeros_file = os.path.join(BASE_DIR, "..", "compute_zeros", "results", "zeros_found.txt")
with open(zeros_file, "r") as f:
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

# Create sequences for LSTM (use the past 5 zeros to predict the next one)
sequence_length = 5
X, y = [], []
for i in range(len(imag_parts_normalized) - sequence_length):
    X.append(imag_parts_normalized[i:i + sequence_length])
    y.append(imag_parts_normalized[i + sequence_length])
X = np.array(X)
y = np.array(y)

# Reshape X for LSTM [samples, time steps, features]
X = X.reshape(X.shape[0], X.shape[1], 1)

# Save the data next to this script
data_dir = os.path.join(BASE_DIR, "data")
os.makedirs(data_dir, exist_ok=True)
np.save(os.path.join(data_dir, "X.npy"), X)
np.save(os.path.join(data_dir, "y.npy"), y)
np.save(os.path.join(data_dir, "imag_parts.npy"), imag_parts)
# Save the scaler using pickle so it can be loaded reliably
with open(os.path.join(data_dir, "scaler.pkl"), "wb") as f:
    pickle.dump(scaler, f)

print(f"Prepared {len(X)} sequences for training.")
print(f"Data saved to 'data/' directory.")
