# shortest path in undirected graph
from heapq import  heappush, heappop
def djikstra(V, adj, src):
    heap=[]
    dist=[float('inf')]*V
    dist[src]=0
    heappush(heap, (0, src))

    while len(heap)>0:
        item = heappop(heap)
        for neighbor in adj[item[1]]:
            if dist[neighbor[0]]>neighbor[1]+ dist[item[1]]:
                dist[neighbor[0]] = neighbor[1]+ dist[item[1]]
                heappush(heap,(dist[neighbor[0]], neighbor[0]) )
    return dist