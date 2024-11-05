import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {}

num_vertices = int(input("\nEnter the number of vertices: "))
for i in range(num_vertices):
    vertex = input("Enter vertex name: ")
    graph[vertex] = {}

num_edges = int(input("\nEnter the number of edges: "))
print()
for i in range(num_edges):
    u = input("Enter the starting vertex of the edge: ")
    v = input("Enter the ending vertex of the edge: ")
    weight = int(input("Enter the weight of the edge: "))
    print()
    graph[u][v] = weight
    graph[v][u] = weight

start_vertex = input("\nEnter the starting vertex: ")
shortest_paths = dijkstra(graph, start_vertex)
print(f"Shortest paths from {start_vertex}: {shortest_paths}")