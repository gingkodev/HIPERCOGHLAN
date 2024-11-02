import networkx as nx
import matplotlib.pyplot as plt
import random

# Theory:
# In network theory, nodes represent entities, and edges connect nodes with relationships. 
# Here, each node is a point, and edges connect points won consecutively by the same player. 
# Larger connected components indicate momentum, showing dominance and streaks.

# Parameters
num_points = 20  # Total points in this small example
results = [random.choice(["A", "B"]) for _ in range(num_points)]  # Random sequence of point wins

# Create the graph
G = nx.Graph()
for i, result in enumerate(results):
    G.add_node(i, player=result)

# Connect nodes with the same player for consecutive points
for i in range(num_points - 1):
    if results[i] == results[i + 1]:  # Connect if same player won consecutive points
        G.add_edge(i, i + 1)

# Visualization with colored nodes for each player
color_map = ["red" if G.nodes[i]['player'] == "A" else "blue" for i in G.nodes]
nx.draw(G, with_labels=True, node_color=color_map, font_weight='bold')
plt.title("Network Graph of Point Dependencies")
plt.show()
