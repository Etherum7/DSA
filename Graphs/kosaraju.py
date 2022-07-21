class Solution:
    def topoSort(self, v, adj, st, visited):
        visited[v] = 1
        for neighbour in adj[v]:
            if not visited[neighbour]:
                self.topoSort(neighbour, adj, st, visited)
        st.append(v)

    def transposeGraph(self, V, adj, visited):
        adj2 = []
        for _ in range(V):
            adj2.append([])
        for vertex in range(V):
            visited[vertex] = 0
            for neighbour in adj[vertex]:

                adj2[neighbour].append(vertex)
        return adj2

    def dfs(self, v, adj2, visited):
        visited[v] = 1
        for neighbour in adj2[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, adj2, visited)
    # Function to find number of strongly connected components in the graph.

    def kosaraju(self, V, adj):
        # code here
        st = []
        visited = [0]*V
        for i in range(V):
            if not visited[i]:
                self.topoSort(i, adj, st, visited)
        print(st)
        adj2 = self.transposeGraph(V, adj, visited)
        print(adj2)
        res = 0
        while len(st) > 0:
            t = st.pop()
            if not visited[t]:
                print(t)
                self.dfs(t, adj2, visited)
                res += 1
        return res
ob=Solution()
adj=[[2,3],[0],[1],[4],[]]
print(ob.kosaraju(5,adj))