import numpy as np
import matplotlib.pyplot as plt
import random

# Theory:
# In the Ising model, each node (or lattice point) represents a particle's "spin" 
# (a magnetic property), which can be either up or down. Neighboring spins tend to 
# align with each other, forming clusters. Here, we treat each point in a tennis game 
# as a node in a lattice. Each node's "spin" represents the winning player: 
# - +1 for Player A (indicating Player A won the point) 
# - -1 for Player B (indicating Player B won the point)
# This forms clusters in our visualization, showing areas where one player 
# dominates over a series of points.

# Parameters
num_points = 100  # Total number of points in the lattice
lattice_size = 10  # Size of the lattice (10x10 grid)

# Randomly generate who wins each point (1 for Player A, -1 for Player B)
# In a real-world scenario, this data could come from live match updates.
points = [random.choice([1, -1]) for _ in range(num_points)]
lattice = np.reshape(points, (lattice_size, lattice_size))

# Plotting
plt.figure(figsize=(6, 6))
# We use a color map where red represents Player A's points and blue represents Player B's points.
plt.imshow(lattice, cmap='bwr', interpolation='nearest')
plt.colorbar(ticks=[-1, 1], label="Player (1 = A, -1 = B)")
plt.title("Lattice-Based Momentum Visualization")
plt.xlabel("Point Index (X)")
plt.ylabel("Point Index (Y)")
plt.show()
