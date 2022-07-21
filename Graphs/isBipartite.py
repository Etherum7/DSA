from queue import Queue


class Solution:
    def bfsCheck(self, adj, v, color, q):
        color[v] = 0
        q.put(v)

        while not q.empty():
            t = q.get()
            for neighbour in adj[t]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 ^ color[t]
                    q.put(neighbour)

                elif color[neighbour] == color[t]:
                    return False
        return True
    def dfsCheck(self, v, adj, color , val):
        color[v]=val
        for neighbour in adj[v]:
            if color[neighbour]==-1:
                if not self.dfsCheck(neighbour,adj, color, 1^val):
                    return False
            elif color[v]==color[neighbour]:
                return False
        return True

    def isBipartiteDFS(self, V, adj):
        color=[-1]*V
        for i in range(V):
            if color[i]==-1:
                if not self.dfsCheck(i, adj, color, 0):
                    return False
        return True


    def isBipartiteBFS(self, V, adj):
        # code here
        color = [-1]*(V)
        q = Queue()
        for i in range(V):
            if color[i] == -1:
                if not self.bfsCheck(adj, i, color, q):
                    return False
        return True
adj = []
adj.append([1,3])
adj.append([0,2])
adj.append([1,3])
adj.append([0,2])

ob=Solution()
print(ob.isBipartiteBFS(4, adj))
print(ob.isBipartiteBFS(4, adj))