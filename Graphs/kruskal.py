from heapq import heappush, heappop
# def sortAdj(V, adj):
#     heap=[]
#     for i in range(V):
#         for neighbour, weight in adj[i]:
#             heappush(heap, (weight, i, neighbour))
#     return heap
# def findPar(u, parent):
#     if u==parent[u]:
#         return u
#     parent[u]= findPar(parent[u], parent)
#     return parent[u]
    
# def union(u, v, parent, rank):
#     u=findPar(u,parent)
#     v=findPar(v,parent)

#     if u==v:
#         return
#     if rank[u]>rank[v]:
#         parent[v]=u
#     elif rank[v]>rank[u]:
#         parent[u]=v
#     else:
#         parent[v]=u
#         rank[u]+=1

# def kruskals(V, adj):
#     heap = sortAdj(V, adj)
#     parent=[i for i in range(V)]
#     rank=[0]*V
#     costMst=0
#     mst=[]
#     for item in heap:
#         u=item[1]
#         v=item[2]
#         if findPar(u)!=findPar(v):
#             costMst+=item[0]
#             mst.append((item[1],item[2]))
#             union(u,v , parent, rank)
#             # add to res


def sortAdj(V, adj):
    heap=[]
    for i in range(V):
        for nb, wt in adj[i]:
            heappush(heap, (wt, nb, i))
    return heap
def findPar(parent, u):
    if u==parent[u]:
        return u
    parent[u]=findPar(parent,parent[u])
    return parent[u]
def union(u, v, parent, rank):
    up=findPar(parent,u)
    vp=findPar(parent,v)
    if(up==vp) :return
    if rank[up]>rank[vp]:
        parent[vp]=up
    elif rank[vp]>rank[up]:
        parent[up]=vp
    else:
        parent[vp]=up
        rank[up]+=1

def kruskals1(V, adj):
    heap=sortAdj(V, adj)
    parent=[i for i in range(V)]
    rank=[0]*V
    costMst=0
    mst=[]
    for (wt, u, v) in heap:
        if findPar(u)!=findPar(v):
            union(u, v, parent, rank)
            costMst+=wt
            mst.append((u,v))



