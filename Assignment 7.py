# DFS using Adjacency Matrix

def dfs(graph, visited, vertex):
    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(len(graph)):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(graph, visited, i)

n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting vertex (0 to n-1): "))

visited = [False] * n

print("DFS Traversal:")
dfs(graph, visited, start)
