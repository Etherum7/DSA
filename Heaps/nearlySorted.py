#User function Template for python3
from heapq import heappush , heappop, heapify
class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        res=[]
        heap=[]
        for i in range(k+1):
            heappush(heap, a[i])
        i=k+1
        while len(heap):
            res.append(heappop(heap))
            if i< n : heappush(heap, a[i])
            i+=1
        return res