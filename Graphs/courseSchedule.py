class Solution:
    def topoSort(self, v, adj, st, visited, recStack):
        visited[v] = 1
        recStack[v] = 1
        for neighbour in adj[v]:
            if not visited[neighbour]:
                if self.topoSort(neighbour, adj, st, visited, recStack):
                    return True
            elif visited[neighbour] ==1 and recStack[neighbour]==1:
                return True
        recStack[v] = 0
        st.append(v)
        return False

    def makeGraph(self, n, prereq):
        adj = []
        for _ in range(n):
            adj.append([])

        for pre in prereq:
            adj[pre[0]].append(pre[1])
        return adj

    def findOrder(self, n, m, prerequisites):
        # Code here
        adj = self.makeGraph(n, prerequisites)
        # print(adj)
        st = []
        visited = [0]*n
        recStack = [0]*n
        for i in range(n):
            if not visited[i]:
                # print(st)
                if self.topoSort(i, adj, st, visited, recStack):
                    return []
        # print(st)

        return st
ob=Solution()
print(ob.findOrder(2, 1, [[1,0]]))