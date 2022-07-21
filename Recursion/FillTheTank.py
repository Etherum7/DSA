#User function Template for python3

import sys
sys.setrecursionlimit(10**5)
class Solution:
    def util(self,cur, adj, n, cap, prev):
        ans=cap[cur-1]
        maxAns=0
        children=0
        for child in adj[cur]:
            if child==prev:
                continue
            children+=1
            tempAns=self.util(child, adj, n, cap, cur)
            if tempAns==-1:
                return -1
            maxAns=max(maxAns, tempAns)
        ans+=children * maxAns
        return -1 if ans > 1e18  else ans
            
    def minimum_amount (self, Edges, num, start, Cap):
        # code here
        adj=[[] for _ in range(num+1)]
        for (u,v) in Edges:
            adj[u].append(v)
            adj[v].append(u)
        return self.util(start, adj, num, Cap, -1)