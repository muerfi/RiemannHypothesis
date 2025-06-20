# machine_learning/lstm_model.py
# Author: Murphy
# Date: March 2025
# Description: Train an LSTM model to predict the positions of non-trivial zeros.

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error
import pickle
import os

# Directory paths relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
VIS_DIR = os.path.join(BASE_DIR, "visualizations")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load the prepared data
X = np.load(os.path.join(DATA_DIR, "X.npy"))
y = np.load(os.path.join(DATA_DIR, "y.npy"))
# Load the scaler saved during data preparation
with open(os.path.join(DATA_DIR, "scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)

# Split into training and testing sets (80% train, 20% test)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Build the LSTM model
model = Sequential([
    LSTM(50, activation='tanh', input_shape=(X.shape[1], 1), return_sequences=False),
    Dense(25),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=16, validation_split=0.1, verbose=1)

# Make predictions
y_pred = model.predict(X_test)

# Inverse transform the predictions and actual values
y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()
y_pred_inv = scaler.inverse_transform(y_pred.reshape(-1, 1)).flatten()

# Compute the mean squared error
mse = mean_squared_error(y_test_inv, y_pred_inv)
print(f"Mean Squared Error on Test Set: {mse:.4f}")

# Save the predictions and actual values for visualization
os.makedirs(VIS_DIR, exist_ok=True)
np.save(os.path.join(VIS_DIR, "y_test.npy"), y_test_inv)
np.save(os.path.join(VIS_DIR, "y_pred.npy"), y_pred_inv)

# Save the model
os.makedirs(MODEL_DIR, exist_ok=True)
model.save(os.path.join(MODEL_DIR, "lstm_model.h5"))

print("Model training complete. Predictions saved to 'visualizations/' directory.")
print(f"Model saved to '{os.path.join('models', 'lstm_model.h5')}'.")
