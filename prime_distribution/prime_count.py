# prime_distribution/prime_count.py
# Author: Murphy
# Date: March 2025
# Description: Compute the exact number of primes up to x using the Sieve of Eratosthenes.

import numpy as np

def sieve_of_eratosthenes(n):
    """Compute the number of primes up to n using the Sieve of Eratosthenes."""
    if n < 2:
        return 0
    # Initialize the sieve array
    is_prime = np.ones(n + 1, dtype=bool)
    is_prime[0:2] = False  # 0 and 1 are not primes
    for i in range(2, int(np.sqrt(n)) + 1):
        if is_prime[i]:
            is_prime[i * i:n + 1:i] = False
    return np.sum(is_prime)

# Test the function for various values of x
x_values = [10**k for k in range(1, 7)]  # x = 10, 100, ..., 1000000
pi_x = [sieve_of_eratosthenes(x) for x in x_values]

# Print results
print("Exact number of primes π(x) for various x:")
for x, count in zip(x_values, pi_x):
    print(f"π({x}) = {count}")
  
