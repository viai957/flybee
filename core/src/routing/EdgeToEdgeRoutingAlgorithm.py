# Edge to edge routing algorithm (which means one edge to onther rather than one node to another)
import networkx as nx
from rtree import index
# Author Vignesh Yaadav
class EdgeToEdgeRoutingAlgorithm:
    def __init__(self, G, spatial_index):
        self.G = G
        self.spatial_index = spatial_index
        
    def shortest_path_coords(self, pickup_coords, dropoff_coords):
        # Find the nearest edges in the graph to the pickup and dropoff coordinates
        pickup_edge =  next(self.spatial_index.nearest((pickup_coords[1], pickup_coords[0])))
        dropoff_edge = next(self.spatial_index.nearest((dropoff_coords[1], dropoff_coords[0])))
        
        # Find the shortest path between the pickup and dropoff edges using A* algorithm
        path = nx.shortest_path(self.G, pickup_edge, dropoff_edge, weight='length')
        
        # Extract the coordinates of the edges along the shortest path
        path_coords = [(self.G.edges[edge]['y'], self.G.edges[edge]['x']) for edge in path]
        
        return path_coords

# Create an instance of the EdgeToEdgeRoutingAlgorithm class
edge_to_edge_routing = EdgeToEdgeRoutingAlgorithm(G, spatial_index)

# Call the shortest_path_coords method
pickup_coords = (40.751231, -73.994148)
dropoff_coords = (40.747638, -73.973999)
path_coords = edge_to_edge_routing.shortest_path_coords(pickup_coords, dropoff_coords)
print(path_coords)