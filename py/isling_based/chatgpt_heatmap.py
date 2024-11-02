import numpy as np
import matplotlib.pyplot as plt

# Theory:
# A heatmap visualizes intensity across an area. Here, we treat each row as a game and each
# column as a point in that game. Each cell’s color intensity represents dominance by a player,
# with positive values indicating Player A’s control and negative values indicating Player B’s.
# By tracking the intensity of clusters, we can see momentum shifts or steady control periods.

# Parameters
num_games = 10
points_per_game = 10

# Generate random dominance values: positive for Player A, negative for Player B
dominance = np.random.choice([-1, 1], size=(num_games, points_per_game)) * np.random.random((num_games, points_per_game))

# Plotting
plt.figure(figsize=(8, 6))
plt.imshow(dominance, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label="Dominance Level (Player A: Positive, Player B: Negative)")
plt.title("Heatmap of Game Progression")
plt.xlabel("Points per Game")
plt.ylabel("Game Number")
plt.show()
