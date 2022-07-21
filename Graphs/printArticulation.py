# User function Template for python3

import sys
sys.setrecursionlimit(10**6)

# TIP: (copied) : So ultimately it all converges down to finding a back edge for every vertex. So, for that apply a DFS and record the discovery time of every vertex and maintain for every vertex  the earliest discovered vertex that can be reached from any of the vertices in the subtree rooted at . If a vertex  is having a child  such that the earliest discovered vertex that can be reached from the vertices in the subtree rooted at  has a discovery time greater than or equal to , then  does not have a back edge, and thus  will be an articulation point.
class Solution:
    def dfs(self, v, parent, adj, tin, low, timer, visited, res):
        visited[v] = 1
        timer[0] += 1
        low[v] = tin[v] = timer[0]
        child = 0

        for neighbour in adj[v]:
            if neighbour == parent:
                continue
            if not visited[neighbour]:
                self.dfs(neighbour, v, adj, tin, low, timer, visited, res)
                low[v] = min(low[v], low[neighbour])
                if low[neighbour] >= tin[v] and parent != -1:
                    res.add(v)
                child += 1

            else:
                low[v] = min(low[v], tin[neighbour])
        if parent == -1 and child > 1:
            res.add(v)

    # Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        res = set()
        visited = [0]*V
        tin = [-1]*V
        low = [-1]*V
        timer = [0]
        for i in range(V):
            if not visited[i]:
                self.dfs(i, -1, adj, tin, low, timer, visited, res)

        return list(sorted(res)) if len(res) > 0 else [-1]

def dfs(v, parent, adj,res,timer, timeInsertion, visited, lowestTime):
    visited[v]=1
    timer[0]+=1
    timeInsertion[v]=timer[0]
    lowestTime[v]=timer[0]
    children=0
    for nb in adj[v]:
        if nb==parent:
            continue
        if not visited[nb]:
            dfs(nb, v, adj, res,timer, timeInsertion, visited,lowestTime)
            lowestTime[v]=min(lowestTime[v], lowestTime[nb])
            if(lowestTime[nb]>timeInsertion[v] and parent!=-1):
                res.add(v)
            child+=1
        else:
            lowestTime[v]=min(lowestTime[v], timeInsertion[nb])

    if parent==-1 and child>1:
        res.add(v)
            





def findAP(V, adj):
    visited=[0]*V
    timer=[0]
    timeInsertion=[-1]*V
    lowestTime=[-1]*V
    res=set()
    for i in range(V):
        if not visited[i]:
            dfs(i, -1, adj, res,timer, timeInsertion, visited, lowestTime)
    return list(res)