""" 
A* algorithm with heuristic function
This script first uses the osmnx library to load the road network data for the area around the pickup and drop locations, and then it defines the heuristic function that estimates the distance from the current node to the goal node. Then it uses the A* algorithm to find the shortest path. It uses a priority queue to keep track of the frontier and uses the heuristic function to guide the search. It stores the cost of each node and the previous node in the path. It finally finds the shortest route based on the previous dictionary and prints the result on the console.

Please note that this script uses Bangalore, India as an example, you will need to change it accordingly and also you need to have the OpenStreetMap data  """
import osmnx as ox
import heapq
# Author Vignesh Yaadav
def heuristic(node):
    return ox.great_circle_vec(ox.get_node_coordinates(node), drop)

# Find the shortest path using the A* algorithm
start = ox.get_nearest_node(G, pickup)
end = ox.get_nearest_node(G, drop)

# Set of visited nodes
visited = set()

# Priority queue for the frontier
frontier = [(0, start)]

# Dictionary to store the previous node for each node
previous = {}

# Dictionary to store the cost for each node
cost = {start: 0}

while frontier:
    current_cost, current_node = heapq.heappop(frontier)

    # Check if the current node is the goal node
    if current_node == end:
        break

    # Skip the current node if it has already been visited
    if current_node in visited:
        continue

    # Mark the current node as visited
    visited.add(current_node)

    # Check all the neighboring nodes
    for neighbor, data in G[current_node].items():
        new_cost = cost[current_node] + data.get('length')

        # Update the cost and previous node if a better path is found
        if neighbor not in cost or new_cost < cost[neighbor]:
            cost[neighbor] = new_cost
            priority = new_cost + heuristic(neighbor)
            previous[neighbor] = current_node
            heapq.heappush(frontier, (priority, neighbor))

# Find the shortest route based on the previous dictionary
path = []
while end != start:
    path.append(end)
    end = previous[end]
path.append(start)
path = path[::-1]

