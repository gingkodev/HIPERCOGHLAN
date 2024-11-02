import numpy as np
import matplotlib.pyplot as plt

# Theory:
# Cellular automata consist of a grid of "cells," each of which changes state according to a set of rules. 
# Each cell represents a point in a tennis match, with:
# - +1 (Player A won the point)
# - -1 (Player B won the point)
# Rules:
# - If a player has won recent points (momentum), the next cell is likely to continue in that player's favor.
# - If momentum shifts (the other player wins a point), the direction may reverse.
# This approach highlights scoring trends visually across games.

# Parameters
num_games = 10         # Number of games
points_per_game = 10   # Number of points per game
probability_flip = 0.3 # Probability to switch winning player in each point

# Initialize the CA grid with random initial states (+1 for Player A, -1 for Player B)
# Create a 2D array where rows are games, columns are points in the game.
ca_grid = np.zeros((num_games, points_per_game), dtype=int)
initial_winner = np.random.choice([1, -1])  # Choose an initial winner randomly
ca_grid[0, 0] = initial_winner

# Generate CA grid based on "momentum rules"
for game in range(num_games):
    for point in range(1, points_per_game):
        if np.random.rand() > probability_flip:  # Follow the previous point's winner with probability 1 - flip rate
            ca_grid[game, point] = ca_grid[game, point - 1]
        else:
            ca_grid[game, point] = -ca_grid[game, point - 1]  # Switch to the other player

    # For subsequent games, base the first point on the outcome of the previous game
    if game < num_games - 1:
        ca_grid[game + 1, 0] = ca_grid[game, -1]

# Visualization
plt.figure(figsize=(8, 6))
# Red for Player A (won the point), blue for Player B (won the point)
plt.imshow(ca_grid, cmap='bwr', interpolation='nearest')
plt.colorbar(ticks=[-1, 1], label="Player (1 = A, -1 = B)")
plt.title("Cellular Automaton of Tennis Points")
plt.xlabel("Point Number within Game")
plt.ylabel("Game Number")
plt.show()
