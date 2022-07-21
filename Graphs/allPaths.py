# User function Template for python3


class Solution:
    def makeGraph(self, edges, n):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        return adj

    def dfs(self, v, adj, d, cnt, visited):
        visited[v] = 1
        if v == d:
            cnt[0] += 1
            visited[d] = 0
            return
        for nb in adj[v]:
            if not visited[nb]:
                self.dfs(nb, adj, d, cnt, visited)
        visited[v] = 0

    def possible_paths(self, edges, n, s, d):
        # Code here
        adj = self.makeGraph(edges, n)
        cnt = [0]
        visited = [0]*n
        self.dfs(s, adj, d, cnt, visited)
        return cnt[0]
