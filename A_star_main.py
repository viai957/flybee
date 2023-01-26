# main.py

import csv
from rtree import index
import shortest_path_astar

# Load the data from the CSV file
with open('test-trips.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

# Create a new column in the data for the path coordinates
for row in data:
    row['path_coords'] = None

# Load the graphml file
G = nx.read_graphml('newyork_road_network.graphml')

# Create a spatial index for the graph
spatial_index = index.Index()
for i, node in enumerate(G.nodes()):
    spatial_index.insert(i, (G.nodes[node]['x'], G.nodes[node]['y'], G.nodes[node]['x'], G.nodes[node]['y']))