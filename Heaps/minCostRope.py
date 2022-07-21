#User function Template for python3
from heapq import heapify, heappush,heappop
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        # code here
        if n==1:
            return 0
        
        heapify(arr)
        res=heappop(arr)+heappop(arr)
        heappush(arr, res)
        total=res
        while len(arr)>=2:
            t1=heappop(arr)
            t2=heappop(arr)
            total+=t1+t2
            heappush(arr, t1+t2)
        return total