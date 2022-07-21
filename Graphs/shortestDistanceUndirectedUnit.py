from queue import Queue
def shortestDistanceUD(V,src, dst, adj):
    dist=[float('inf')]*V
    q=Queue()
    q.put(src)
    dist[src]=0
    while not q.empty():
        t=q.get()
        for neighbour in adj[t]:
            if 1+dist[t]<dist[neighbour]:
                dist[neighbour]=1+dist[t]
                q.put(neighbour)
    return dist[dst]



