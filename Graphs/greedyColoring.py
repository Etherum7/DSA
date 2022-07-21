def greedyColoring(adj, V):
    color = [-1]*V
    available = [1]*V
    # np ndicates color
    color[0] = 0
    # available[0] = 0

    for i in range(1, V):
        available = [1]*V
        for neighbour in adj[i]:
            if color[neighbour] != -1:
                available[color[neighbour]] = 0
        for j in range(V):
            if available[j] != 0:
                color[i] = j
                available[j] = 0
                break
    return color


def addEdge(adj, v, w):

    adj[v].append(w)

    # Note: the graph is undirected
    adj[w].append(v)
    return adj


g1 = [[] for i in range(5)]
g1 = addEdge(g1, 0, 1)
g1 = addEdge(g1, 0, 2)
g1 = addEdge(g1, 1, 2)
g1 = addEdge(g1, 1, 3)
g1 = addEdge(g1, 2, 3)
g1 = addEdge(g1, 3, 4)
print("Coloring of graph 1 ")
print(greedyColoring(g1, 5))

g2 = [[] for i in range(5)]
g2 = addEdge(g2, 0, 1)
g2 = addEdge(g2, 0, 2)
g2 = addEdge(g2, 1, 2)
g2 = addEdge(g2, 1, 4)
g2 = addEdge(g2, 2, 4)
g2 = addEdge(g2, 4, 3)
print("\nColoring of graph 2")
print(greedyColoring(g2, 5))
