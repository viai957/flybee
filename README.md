# Flybee
# Open Source routing System

## Overview
This repository contains a Python implementation of a routing engine for road networks, similar to GraphHopper. The routing engine is built using the NetworkX library and includes several different routing algorithms, such as Dijkstra, A* bidirectional, and Contraction Hierarchy (CH). It also includes a spatial index for efficient nearest-neighbor searches and a utility for loading road network data in the GraphML format.


## Installation

To use the routing engine, you will need to have Python 3.6 or higher installed on your system. You will also need to install the following dependencies:

- NetworkX (2.5 or higher)
- OSMNX (0.14 or higher)
- RTree (0.9 or higher)
- Sharply (1.7 or higher)
- Python-Levenshtein

To install the package, clone the repository and install the required dependencies using pip:

```bash
git clone https://github.com/viai957/flybee
cd flybee/core/src/routing
pip install -r requirements.txt
```
    
## Usage

The package includes several different modules for different functionality:

- graph_utils.py: Contains functions for loading and preprocessing road network data in the GraphML format.
- spatial_index.py: Implements a spatial index for efficient nearest-neighbor searches.
- shortest_path.py: Implements several different routing algorithms, including Dijkstra, A* bidirectional, and Contraction Hierarchy (CH).

To use the package, first load the road network data using the ``load_graphml`` function from ``graph_utils.py``. Then, create a spatial index using the create_spatial_index function from ``spatial_index.py``. Finally, use one of the routing algorithms in `shortest_path.py` to find the shortest path between two points on the road network.

For example, to find the shortest path between two coordinates using the Dijkstra algorithm:


```
from graph_utils import load_graphml
from spatial_index import create_spatial_index
from shortest_path import shortest_path_coords_dijkstra

# Load the road network data
G = load_graphml('path/to/road_network.graphml')

# Create a spatial index for the road network graph
spatial_index = index.Index()
for node, data in G.nodes(data=True):
    spatial_index.insert(node, (data['y'], data['x'], data['y'], data['x']))

# Set the coordinates of the pickup and dropoff points
pickup_coords = (40.751231, -73.994148)
dropoff_coords = (40.747638, -73.973999)

# Create an instance of the AStarBidirection class
astar = AStarBidirection(G, spatial_index)

# Find the shortest path between the pickup and dropoff points
path_coords = ast

```

## Authors

- [@vignesh](https://www.github.com/viai957)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Features

This is a venilla version of this routing engine much more to come in, please share your hand by contributing

- A - B routing (Find the shortest path given the pickup and drop coordinates)
- Pooling (Finding a optimal dynamic path based on available space, pickup and drop)
- Spacial Metrix ( A recomputed Spacial Matrix file with also dynamic weathar updates)
- Distance Matrix ( By Tweaking the Distance Matrix the efficency could be increased)


## 🚀 About Me
I'm a Ml tinkerer working on few projects made me realize building an Open Sourcer Routing sytem with API calls with no cost conversion would make a huge diffrence for small scale startups to test few cases with easy to understand python code and proper documentation. You could come across many other open source routing engine but most of them are built on 20 years old technology in todays day and age it's archaic. To accommodate current day business needs we need to build robust product on the latest technology
