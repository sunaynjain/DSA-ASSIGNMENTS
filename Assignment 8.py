# BFS using Adjacency List

def bfs(graph, start):
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

print("Enter edges (u v):")

for i in range(e):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)  # For undirected graph

start = int(input("Enter starting vertex: "))

print("BFS Traversal:")
bfs(graph, start)
