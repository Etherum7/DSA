from queue import Queue


def isCyclicDFS(v, adj, visited, recStack):
    visited[v] = 1
    recStack[v] = 1
    for neighbour in adj[v]:
        if not visited[neighbour]:
            if isCyclicDFS(neighbour, adj, visited, recStack):
                return True
        elif visited[neighbour] and recStack[neighbour] == 1:
            return True
    recStack[v] = 0
    return False


def cycleDirected(V, adj):
    visited = [0]*V
    recStack = [0]*V
    for i in range(V):
        if not visited[i]:
            if isCyclicDFS(i, adj, visited, recStack):
                return True
    return False


def isCyclicBFS(V, adj):
    q = Queue()
    indegree = [0]*V
    for i in range(V):
        for neighbour in adj[i]:
            indegree[neighbour] += 1
    for i in range(V):
        if indegree[i] == 0:
            q.put(i)
    cnt = 0
    while not q.empty(): 
        t = q.get()
        cnt += 1
        for neighbour in adj[t]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                q.put(neighbour)
        if cnt > V:
            return True
    if cnt == V:
        return False
