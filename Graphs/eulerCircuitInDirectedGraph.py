# all nonzero in single strongly connected
# ind=outd

# len of scc=1 after removing degree 0
def topoSort(i, adj, visited, st):
    visited[i] = True
    for neighbour in adj[i]:
        if not visited[neighbour]:
            topoSort(neighbour, adj, visited, st)
    st.append(i)


def transpose(V, adj, visited):
    adj1 = [[] for i in range(V)]
    for i in range(V):
        visited[i] = False

        for n in adj[i]:
            adj1[n].append(i)
    return adj1


def dfs(i, adj, visited, op):
    visited[i] = True
    op.append(i)
    for neighbour in adj[i]:
        if not visited[neighbour]:
            dfs(neighbour, adj, visited, op)


def kosaraju(V, adj):
    visited = [False]*V
    st = []
    topoSort(0, adj, visited, st)
    if len(st) != V:
        return 0
    adj = transpose(V, adj, visited)
    st = st[::-1]
    res = []
    while len(st):
        t = st.pop()
        if not visited[t]:
            op = []
            dfs(t, adj, visited, op)
            res.append(op)
    # print(res)
    return 1 if len(res) == 1 else 0


def eulerDirected(V, adj):
    for i in range(V):
        if len(adj[i]) == 0:
            adj.pop(i)
    V = len(adj)
    if not kosaraju(V, adj):
        return 0
    ind = [0]*V
    oud = [0]*V
    for i in range(V):
        oud[i] = len(adj[i])
        for n in adj[i]:
            ind[n] += 1
    # print(ind, oud)
    for i in range(V):
        
        if ind[i] != oud[i]:
            return 0
    

    return 1
g=[[2,3],[0],[1],[4],[0]]
print(eulerDirected(5,g))