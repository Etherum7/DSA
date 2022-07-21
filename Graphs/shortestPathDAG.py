def topoSort(v, adj, st, visited):
    visited[v]=1
    for neighbor in adj[v]:
        if not visited[neighbor[0]]:
            topoSort(neighbor[0], adj, st, visited)
    st.append(v)

def shortestDistanceDAG(V, adj, src):
    st=[]
    visited=[0]*V
    dist=[float('inf')]*V
    for i in range(V):
        if not visited[i]:
            topoSort(i, adj, st, visited)
    dist[src]=0

    while len(st)>0:
        t=st.pop()
        if dist[t]<float('inf'):
            for neighbor in adj[t]:
                if dist[neighbor[0]]> neighbor[1]+dist[t]:
                    dist[neighbor[0]]=dist[t]+neighbor[1]
    return dist

# def shortest
def topoSort2(v, adj, visited, st):
    visited[v]=1
    for nb in adj[v]:
        if not visited[nb[0]]:
            topoSort2(nb[0], adj, visited, st)
    st.append(v)


def shortest(src, V, adj):
    st=[]
    visited=[0]*V
    for i in range(V):
        if not visited[i]:
            topoSort2(i, adj, visited, st)
    dist=[float('inf')]*V
    dist[src]=0
    while len(st):
        top=st.pop()
        if dist[top]!=float('inf'):
            for nb,wt in adj[top]:
                if dist[nb]>dist[top]+wt:
                    dist[nb]=dist[top]+wt
    return dist




