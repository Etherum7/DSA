from queue import Queue
def isCyclicBFS(adj, visited , v):
    q=Queue()
    visited[v]=True
    q.put((v, -1))
    while not q.empty():
        t, prev = q.get()
        for neighbour in adj[t]:
            if visited[neighbour] and neighbour != prev:
                return True
            if not visited[neighbour]:
                visited[neighbour]=True
                q.put((neighbour, t))
    return False

def isCyclicUnDirectedBFS(adj , V ):
    visited=[False]*(V+1)
    for i in range(V):
        if not visited[i]:
            if isCyclicBFS(adj , visited, 1):
                return True
    return False

def isCyclicDFS(adj , visited, v, prev):
    visited[v]=True
    for neighbour in adj[v]:
        if visited[neighbour] and prev != neighbour:
            return True
        if not visited[neighbour]:
            isCyclicDFS(adj, visited, neighbour, v)
    return False
    
def isCyclicUnDirectedDFS(adj, V):
    visited=[False]*(V+1)
    for i in range(V):
        if not visited[i]:
            if isCyclicDFS(adj, visited, i, -1 ):
                return True
    return False


adj1 = [[], [2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 3, 5], [3, 4, 6, 7], [5], [5]]
adj2 = [[], [2, 4], [3], [], [2, 6], [4], []]
adj3 = [[], [2], [1], [], [5, 6, 8, 7], [4, 6, 7, 8],
        [4, 5, 7, 8], [4, 5, 6, 8], [4, 5, 6, 7]]

adj4=[[],[2,3], [1], [1]]

print('BFS')
print(isCyclicUnDirectedBFS(adj1, 7))
print(isCyclicUnDirectedBFS(adj2, 6))
print(isCyclicUnDirectedBFS(adj3, 8))
print(isCyclicUnDirectedBFS(adj4, 3))
print('\nDFS')
print(isCyclicUnDirectedDFS(adj1, 7))
print(isCyclicUnDirectedDFS(adj2, 6))
print(isCyclicUnDirectedDFS(adj3, 8))
print(isCyclicUnDirectedDFS(adj4, 3))
