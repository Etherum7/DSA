# User function Template for python3
from queue import Queue


class Solution:

    # Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        # code here

        if d in adj[c] and c in adj[d]:
            adj[c].remove(d)
            adj[d].remove(c)
        else:
            return 0

        q = Queue()
        visited = [0]*V
        q.put(0)

        cnt = 0
        for i in range(V):
            if not visited[i]:
                cnt += 1
                if cnt >= 2:
                    return 1
                else:
                    while not q.empty():
                        t = q.get()
                        visited[t] = 1
                        for n in adj[t]:
                            if not visited[n]:

                                q.put(n)
        return 0


#{
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)

        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i]))

        c,d=map(int,input().split())
        ob = Solution()

        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends

# working
def isBridge(self, V, adj, c, d):
        def dfs(node,adj,vis):
            vis[node]=1
            for j in adj[node]:
                if vis[j]==0:
                    dfs(j,adj,vis)
        vis1=[0]*V   
        initial=0
        for i in range(V):
            if vis1[i]==0:
                initial+=1
                dfs(i,adj,vis1)
        
        vis2=[0]*V
        if d in adj[c]:
            adj[c].remove(d)
        if c in adj[d]:
            adj[d].remove(c)
        final=0
        for i in range(V):
            if vis2[i]==0:
                final+=1
                dfs(i,adj,vis2)
        if initial==final:
            return 0
        else:
            return 1