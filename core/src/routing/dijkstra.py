import heapq

def dijkstra(graph, start):
    # Create a priority queue to store the distances of the unvisited nodes
    pq = []
    heapq.heappush(pq, (0, start))

    # Initialize the distances of all nodes to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a dictionary to store the previous node of each node in the shortest path
    previous = {node: None for node in graph}

    while pq:
        # Extract the node with the shortest distance
        current_distance, current_node = heapq.heappop(pq)

        # Skip the node if it has been visited
        if current_distance > distances[current_node]:
            continue

        # Update the distances of the neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

# Example graph
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 1, 'E': 3},
    'C': {'B': 4, 'D': 2, 'E': 5},
    'D': {'E': 1},
    'E': {}
}

distances, previous = dijkstra(graph, 'A')
print("Distances from A:", distances)
print("Previous nodes:", previous)
