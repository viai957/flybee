# flybee
Open Sorce Routing Algorithm
# Overview
Paragraph 1
This repository contains a routing engine built in Python that uses various algorithms to find the shortest path between two coordinates. The engine is designed to work with OpenStreetMap data and can be easily integrated into any application that requires routing functionality.

Paragraph 2
## Installation
To use the routing engine, you will need to have Python 3.6 or higher installed on your system. You will also need to install the following dependencies:

NetworkX
-OSMNX
-RTree
-Rtree
-Python-Levenshtein
*You can install these dependencies by running the following command: *

##Copy code
`pip install networkx osmnx rtree python-levenshtein`

##Usage
Passage 3
The routing engine can be used to find the shortest path between two coordinates using different algorithms. Currently, the following algorithms are supported:

Dijkstra
A*
Bidirectional Dijkstra
A* bidirectional
To use the routing engine, you will need to provide it with a graph file in GraphML format. You can create a graph file using OSMNX by specifying the bounding box of the area for which you want to create the graph.

Once you have the graph file, you can use the RoutingEngine class to find the shortest path between two coordinates. The class takes in the following parameters:

graph_file: The path to the graph file in GraphML format
algorithm: The algorithm to use to find the shortest path. Can be one of 'dijkstra', 'astar', 'bidijkstra', or 'astar_bidirectional'
spatial_index: The spatial index to use to find the nearest node in the graph to the start and end coordinates
The class also has several methods that can be used to find the shortest path between two coordinates:

find_shortest_path: Finds the shortest path between two coordinates
find_alternative_paths: Finds alternative paths between two coordinates
find_shortest_path_edge_to_edge: Finds the shortest path between two edges
The find_shortest_path method takes in the following parameters:

pickup_coords: The pickup coordinates as a tuple (latitude, longitude)
dropoff_coords: The dropoff coordinates as a tuple
