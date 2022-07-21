def floydWarshall(graph):
    n=len(graph)
    for k in range(0,n):
      for i in range(0,n):
        for j in range(0,n):
            graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])
    