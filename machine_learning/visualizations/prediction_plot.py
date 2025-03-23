# machine_learning/visualizations/prediction_plot.py
# Author: Murphy
# Date: March 2025
# Description: Visualize the predicted vs actual positions of non-trivial zeros.

import numpy as np
import matplotlib.pyplot as plt

# Load the actual and predicted values
y_test = np.load("../visualizations/y_test.npy")
y_pred = np.load("../visualizations/y_pred.npy")

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual Zeros', marker='o', linestyle='-', color='blue')
plt.plot(y_pred, label='Predicted Zeros', marker='x', linestyle='--', color='red')
plt.xlabel('Index')
plt.ylabel('Imaginary Part of Zero')
plt.title('Predicted vs Actual Non-trivial Zeros')
plt.legend()
plt.grid(True)
plt.show()
