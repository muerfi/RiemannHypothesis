# Description: Plot the prime counting function π(x) and its approximation.

import numpy as np
import matplotlib.pyplot as plt
from mpmath import li
import os

# Compute π(x) using a simple sieve
def sieve_of_eratosthenes(n):
    if n < 2:
        return 0
    is_prime = np.ones(n + 1, dtype=bool)
    is_prime[0:2] = False
    for i in range(2, int(np.sqrt(n)) + 1):
        if is_prime[i]:
            is_prime[i * i:n + 1:i] = False
    return np.sum(is_prime)

# Compute π(x) and Li(x) for various x
x_values = np.logspace(1, 5, 100)
pi_x = [sieve_of_eratosthenes(int(x)) for x in x_values]
li_x = [float(li(x)) for x in x_values]

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, pi_x, label='π(x)', color='blue')
plt.plot(x_values, li_x, label='Li(x)', linestyle='--', color='red')
plt.xscale('log')
plt.xlabel('x (log scale)')
plt.ylabel('Number of Primes')
plt.title('Prime Counting Function π(x) vs Li(x)')
plt.legend()
plt.grid(True)

# Save the plot
os.makedirs("images", exist_ok=True)
plt.savefig("images/prime_counting.png", dpi=300, bbox_inches='tight')
plt.close()