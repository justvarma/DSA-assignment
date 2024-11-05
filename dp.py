def bellman_ford(graph, num_vertices, start):
    distances = {vertex: float('infinity') for vertex in range(num_vertices)}
    distances[start] = 0

    for i in range(num_vertices - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distances

graph = []
num_vertices = int(input("\nEnter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))
print()
for i in range(num_edges):
    u = int(input(f"Enter the starting vertex of edge {i + 1}: "))
    v = int(input(f"Enter the ending vertex of edge {i + 1}: "))
    weight = int(input(f"Enter the weight of edge {i + 1}: "))
    print()
    graph.append((u, v, weight))

start_vertex = int(input("\nEnter the starting vertex: "))
shortest_paths = bellman_ford(graph, num_vertices, start_vertex)

if shortest_paths:
    print(f"Shortest paths from vertex {start_vertex}: {shortest_paths}")