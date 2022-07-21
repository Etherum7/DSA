import sys
sys.setrecursionlimit(10**5)


class Solution:
    def dfs(self, v, N, adj, visited):
        visited[v] = True
        for neighbour in adj[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, N, adj, visited)

    def isConnected(self, V, adj):
        visited = [False]*V
        k = 0
        for k in range(V):
            if len(adj[k]) > 0:
                break
        self.dfs(k, V, adj, visited)
        for i in range(V):
            if not visited[i] and len(adj[i]) != 0:
                return False
        return True

    def isEularCircuitExist(self, V, adj):
        # Code here
        if not self.isConnected(V, adj):
            return 0
        odd = 0
        for i in range(V):
            if len(adj[i]) % 2 != 0:
                odd += 1
        if odd == 0:
            return 2
        if odd == 2:
            return 1
        return 0


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isEularCircuitExist(V, adj)
        print(ans)
# } Driver Code Ends
