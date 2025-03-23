# machine_learning/lstm_model.py
# Author: Murphy
# Date: March 2025
# Description: Train an LSTM model to predict the positions of non-trivial zeros.

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error
import pickle

# Load the prepared data
X = np.load("data/X.npy")
y = np.load("data/y.npy")
scaler = pickle.load(open("data/scaler.npy", "rb"))

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
np.save("visualizations/y_test.npy", y_test_inv)
np.save("visualizations/y_pred.npy", y_pred_inv)

# Save the model
model.save("models/lstm_model.h5")

print("Model training complete. Predictions saved to 'visualizations/' directory.")
print("Model saved to 'models/lstm_model.h5'.")
