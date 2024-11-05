from collections import deque

def user_input():
    graph = {}
    n = int(input("\nEnter the number of vertices: "))
    for _ in range(n):
        vertex = input("\nEnter the vertex: ")
        neighbours = input(f"Enter neighbours of {vertex}: ").split()
        graph[vertex] = neighbours
    return graph

def bfs(graph, source):
    if source not in graph:
        print("\nSource vertex not found in the graph.")
        return []

    q = deque([source])
    visited = {source}
    bfs_result = []

    while q:
        vertex = q.popleft()
        bfs_result.append(vertex)
        for neighbour in graph.get(vertex, []):  
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)

    for vertex in graph:
        if vertex not in visited:
            q.append(vertex)
            visited.add(vertex)
            while q:
                vertex = q.popleft()
                bfs_result.append(vertex)
                for neighbour in graph.get(vertex, []):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)

    return bfs_result

graph = user_input()
source = input("\nEnter the source node: ")
bfs_result = bfs(graph, source)
print("BFS Traversal:", bfs_result)