def countTriangle(g, isDirected):
    n=len(g)
    res=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j!=k:
                    if g[i][j] and g[j][k] and g[k][i]:
                        res+=1
    return res//(3 if isDirected==True else 6)
# Create adjacency matrix of an undirected graph
graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]
# Create adjacency matrix of a directed graph
digraph = [[0, 0, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 0, 0],
           [0, 0, 1, 0]]
 
print("The Number of triangles in undirected graph : %d" %
      countTriangle(graph, False))
 
print("The Number of triangles in directed graph : %d" %
      countTriangle(digraph, True))