# prime_distribution/ulam_spiral.py
import numpy as np
import matplotlib.pyplot as plt
from utils.plot_utils import set_plot_style

set_plot_style()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_ulam_spiral(size):
    # Create a grid for the spiral
    grid = np.zeros((size, size), dtype=int)
    x, y = size // 2, size // 2
    num = 1
    step = 1
    direction = 0  # 0: right, 1: up, 2: left, 3: down

    while num <= size * size:
        for _ in range(2):
            for _ in range(step):
                if 0 <= x < size and 0 <= y < size:
                    grid[y, x] = num
                num += 1
                if direction == 0:
                    x += 1
                elif direction == 1:
                    y -= 1
                elif direction == 2:
                    x -= 1
                elif direction == 3:
                    y += 1
            direction = (direction + 1) % 4
        step += 1

    # Mark prime numbers
    prime_grid = np.zeros_like(grid, dtype=bool)
    for i in range(size):
        for j in range(size):
            if grid[i, j] > 0 and is_prime(grid[i, j]):
                prime_grid[i, j] = True

    return prime_grid

# Generate the spiral
size = 51  # Must be odd
prime_grid = generate_ulam_spiral(size)

# Plot the spiral
plt.figure(figsize=(8, 8))
plt.imshow(prime_grid, cmap="binary", interpolation="nearest")
plt.title("Ulam Spiral (Prime Numbers)")
plt.axis("off")
plt.savefig("docs/images/ulam_spiral.png", dpi=300, bbox_inches="tight")
plt.show()
print("Ulam spiral saved as docs/images/ulam_spiral.png")
