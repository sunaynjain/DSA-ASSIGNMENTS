# Prim's Algorithm using Adjacency Matrix

def prim(graph, n):
    visited = [False] * n
    visited[0] = True

    edges_selected = 0
    total_cost = 0

    print("\nMinimum Spanning Tree:")

    while edges_selected < n - 1:
        minimum = float('inf')
        u = -1
        v = -1

        # Find minimum edge from visited to unvisited vertex
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            u = i
                            v = j

        if u == -1:
            print("Graph is disconnected!")
            return

        print(u, "->", v, "Weight:", minimum)

        visited[v] = True
        total_cost += minimum
        edges_selected += 1

    print("Total MST Cost:", total_cost)

n = int(input("Enter number of vertices: "))

graph = []

print("Enter weighted adjacency matrix (0 for no edge):")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

prim(graph, n)
