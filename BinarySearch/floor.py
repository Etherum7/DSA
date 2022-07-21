class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,N,X):
        #Your code here
        start=0
        end=N-1
        res=-1
        while start<=end:
            mid=(start+end)//2
            
            if arr[mid]==X:
                return mid
            elif arr[mid]<X:
                res=max(res,mid)
                start=mid+1
            else:
                end=mid-1
                
        return res