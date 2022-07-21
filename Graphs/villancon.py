class Solution:
    def dfs(self, v, adj, d, col, m):
        p = 1
        for i in range(1, m[0]+1):
            if i not in d:
                d[i] = [v]
                col[v] = i
                break
            else:
                for n in d[i]:
                    if n in adj[v] :
                        p = 0
                        break
                if p==0:
                    col[v] = m[0]+1
                    m[0] += 1
                    d[m[0]] = []
                else:
                    col[v] = i
                    d[i].append(v)
                    break
                
                
        
            
        for n in adj[v]:
            if not col[n]:
                self.dfs(n, adj, d, col, m)

    def minColour(self, N, M, mat):
        # code here
        d = {}
        col = [0]*(M+1)
        col[0]=-1
        adj = [[] for _ in range(M+1)]

        for edge in mat:
            adj[edge[1]].append(edge[0])
        m = [1]
        # print(adj)

        for i in range(1,M+1):
            if col[i] == 0:
                print(col,d)
                self.dfs(i, adj, d, col, m)
        return m[0]-1


ob = Solution()
print(ob.minColour(5, 6, [[1, 3], [2, 3], [3, 4], [1, 4], [2, 5], [3, 5]]))
