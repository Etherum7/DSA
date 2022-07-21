def multistage(graph,N, stages):
    path=[0]*stages
    path[0]=0
    
    d=[0]*N
    cost=[INF]*N
    cost[N-1]=0
    for i in range(N-1, -1,-1):
        for k in range(i+1, N):
            if(graph[i][k]!=INF):
                temp=cost[i]

                # print(graph[i][k])
                cost[i]=min(graph[i][k]+cost[k], cost[i])
                if temp !=cost[i]:
                    d[i]=k
    # print(d)
    for i in range(1,stages):
        path[i]=d[path[i-1]]
    print(path)

    return cost[0]
N=8
INF = 999999999999
stages=4
graph = [[INF, 1, 2, 5, INF, INF, INF, INF],
         [INF, INF, INF, INF, 4, 11, INF, INF],
         [INF, INF, INF, INF, 9, 5, 16, INF],
         [INF, INF, INF, INF, INF, INF, 2, INF],
         [INF, INF, INF, INF, INF, INF, INF, 18],
         [INF, INF, INF, INF, INF, INF, INF, 13],
         [INF, INF, INF, INF, INF, INF, INF, 2],
         [INF, INF, INF, INF, INF, INF, INF, INF]]
print(multistage(graph,N, stages))
