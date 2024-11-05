def floyd_warshall(graph, numVertices):
    distance = [[float('infinity')] * numVertices for i in range(numVertices)]

    for u in range(numVertices):
        for v, weight in graph[u].items():
            distance[u][v] = weight

    for i in range(numVertices):
        distance[i][i] = 0

    for k in range(numVertices):
        for i in range(numVertices):
            for j in range(numVertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

numVertices = int(input("\nEnter the number of vertices: "))
graph = [{} for i in range(numVertices)]

numEdges = int(input("Enter the number of edges: "))
print()
for i in range(numEdges):
    u = int(input(f"Enter the starting vertex of edge {i + 1}: "))
    v = int(input(f"Enter the ending vertex of edge {i + 1}: "))
    weight = int(input(f"Enter the weight of edge {i + 1}: "))
    print()
    graph[u][v] = weight

shortestPaths = floyd_warshall(graph, numVertices)

print("\nShortest paths between all pairs of vertices:")
for row in shortestPaths:
    print(row)
