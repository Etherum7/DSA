from queue import Queue
def topoSortBFS(V, adj):
    q=Queue()
    indegree=[0]*V
    res=[]
    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor]+=1
    for i in range(V):
        if indegree[i]==0:
            q.put(i)  
    while not q.empty():
        t= q.get()
        res.append(t)
        for neighbor in adj[t]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0:
                q.put(neighbor)
    return res
class Solution:
    def dfs(self, v, adj, st, visited):
        visited[v]=1
        for neighbour in adj[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, adj, st,visited)
        st.append(v)
        
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        st=[]
        visited=[0]*V
        for i in range(V):
            if not visited[i]:
                self.dfs(i, adj, st,visited)
        return list(reversed(st))



