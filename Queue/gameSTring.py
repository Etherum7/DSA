#User function Template for python3
from heapq import heappush, heappop
class Solution:
    def minValue(self, s, k):
        d={}
        heap=[]
        for c in s:
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        res=0
        for key, value in d.items():
            
            heappush(heap,(-value, key))
        for i in range(k):
            t=heappop(heap)
            heappush(heap,(t[0]+1, t[1]))
        while len(heap):
            t=heappop(heap)
            res+=(t[0])**2
        return res