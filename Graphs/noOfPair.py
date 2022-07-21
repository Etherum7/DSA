from typing import List
import sys
sys.setrecursionlimit(10**7)


class Solution:
    def findPar(self, u, parent):
        if u == parent[u]:
            return u
        parent[u] = self.findPar(parent[u], parent)
        return parent[u]

    def union(self, u, v, parent):
        u = parent[u]
        v = parent[v]
        if u != v:
            parent[v] = u

    def numberOfPairs(self, a: List[int], pairs: List[List[int]]) -> int:
        # code here
        parent = [i for i in range(a[0])]
        for u, v in pairs:
            self.union(u, v, parent)
        res = 0
        count = [0 for i in range(a[0])]
        for i in range(a[0]):
            pk = self.findPar(i, parent)
            count[pk] += 1
        return sum([i*(a[0]-i) for i in count])//2


ob=Solution()
print(ob.numberOfPairs([5,3],[[0,1],[2,3],[0,4]]))