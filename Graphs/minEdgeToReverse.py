from heapq import heappush, heappop


def djikstra(src, V, adj):
    heap = []
    heappush(heap, (0, src))
    dist = [float('inf')]*V
    dist[src] = 0

    while len(heap):
        node = heappop(heap)
        for neighbour in adj[node[1]]:
            if dist[neighbour[0]] > dist[node[1]]+neighbour[1]:
                dist[neighbour[0]] = dist[node[1]]+neighbour[1]
                heappush(heap,(dist[neighbour[0]], neighbour[0]))
    return dist


def minEdgeToReverse(V, E, edges, src, dst):
    adj = [[] for i in range(V)]
    for u, v in edges:
        adj[u].append([v, 0])
        adj[v].append([u, 1])
    dist = djikstra(src, V, adj)
    return dist[dst]


V = 7
edge = [[0, 1], [2, 1], [2, 3], [5, 1], [4, 5], [6, 4], [6, 3]]
E=len(edge)
print(minEdgeToReverse(V,E, edge, 0,6))

# O(E + V Log V)