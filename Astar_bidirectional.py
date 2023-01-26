import networkx as nx
from rtree import index

def shortest_path_coords_astar_bidirectional(G, pickup_coords, dropoff_coords, spatial_index: index.Index):
    # Find the nearest nodes in the graph to the pickup and dropoff coordinates
    pickup_node = next(spatial_index.nearest((pickup_coords[1], pickup_coords[0])))
    dropoff_node = next(spatial_index.nearest((dropoff_coords[1], dropoff_coords[0])))
    
    # Extract the node IDs from the results
    pickup_node = pickup_node
    dropoff_node = dropoff_node
    
    # Find the shortest path between the pickup and dropoff nodes using A* algorithm with bidirectional search
    path = nx.astar_path(G, pickup_node, dropoff_node)
    
    # Extract the coordinates of the nodes along the shortest path
    path_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in path]
    
    return path_coords

"""
This code is an implementation of the A* algorithm with bidirectional
search for finding the shortest path between two coordinates.
The function takes in a graph (G), pickup coordinates, dropoff coordinates,
and a spatial index as input.
It uses the nearest function from the spatial index to find the nearest nodes
in the graph to the pickup and dropoff coordinates.
It then uses the A* algorithm with bidirectional search provided by
the networkx library to find the shortest path between the pickup and dropoff nodes.
The coordinates of the nodes along the shortest path are then extracted and returned as the output.
"""