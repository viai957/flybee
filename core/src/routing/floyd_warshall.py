def floyd_warshall(graph):
    # Initialize the distance matrix with the weights of the edges
    num_nodes = len(graph)
    distances = [[float('inf') for _ in range(num_nodes)] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                distances[i][j] = 0
            elif graph[i][j] is not None:
                distances[i][j] = graph[i][j]

    # Iterate over all possible intermediate nodes
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances