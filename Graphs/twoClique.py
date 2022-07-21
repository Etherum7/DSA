def getComplement(G, V):
    mat=[[0]*V for i in range(V)]
    for i in range(V):
        for j in range(V):
            if i!=j and G[i][j]==0:
                mat[i][j]=1
    return mat

def isBipartite(v, G, V, color, visited, c):
    color[v]=c
    visited[v]=True
    # print(G)
    for neighbour,val in enumerate(G[v]):
        if val==1:
            # print(val)
            if not visited[neighbour]:
                if not isBipartite(neighbour, G, V, color, visited, 1^c):
                    # print(neighbour)
                    return False
            elif color[neighbour]==color[v]:
                # print(color)
                return False
    return True


def twoClique(G, V):
    G= getComplement(G, V)
    color=[-1]*V
    visited=[False]*V
    for i in range(V):
        if color[i]==-1:
            if isBipartite(i,G, V, color, visited, 0):
               return True

    return False

V = 5
 
G = [[0, 1, 1, 1, 0],
     [1, 0, 1, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [0, 0, 0, 1, 0]]
print(twoClique(G,V))
