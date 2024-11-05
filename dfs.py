def user_input():
    graph = {}
    n = int(input("\nEnter the number of vertices: "))
    for _ in range(n):
        vertex = input("\nEnter the vertex: ")
        neighbours = input(f"Enter neighbours of {vertex}: ").split()
        graph[vertex] = neighbours
    return graph

def dfs(graph, source):
    stack = [source]
    visited = {source}
    dfs_result = []

    while stack:
        vertex = stack.pop()
        dfs_result.append(vertex)
        for neighbour in reversed(graph.get(vertex, [])):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    for vertex in graph:
        if vertex not in visited:
            stack.append(vertex)
            visited.add(vertex)
            dfs_result.extend(dfs(graph, vertex))

    return dfs_result

graph = user_input()
source = input("\nEnter the source vertex: ")
dfs_result = dfs(graph, source)
print("DFS Traversal:", dfs_result)