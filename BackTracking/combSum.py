#{ 
#Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


 # } Driver Code Ends
#User function Template for python3
import sys
sys.setrecursionlimit(10**7)
from itertools import groupby
class Solution:
    def util(self,pos, arr, s, res, op):
        if pos>=len(arr):
            return
        if s==0:
            
            res.append(op)
            return
        if arr[pos]>s:
            return
    
        op1=op[:]
        op1.append(arr[pos])
        self.util(pos, arr, s-arr[pos], res, op1)
        self.util(pos+1, arr, s, res, op)
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,arr, s):
        arr=list(set(arr))
        arr.sort()
        res=[]
        self.util(0, arr, s, res, [])
        # res.sort()
        return res
        return list(k for k,_ in groupby(res))
    
        # code here

ob=Solution()
print(ob.combinationalSum([6, 5 ,6 ,3 ,3 ,4 ,3 ,2 ,2 ,9 ,9],24))