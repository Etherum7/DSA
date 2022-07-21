class Solution:
    def maxSubarrayXOR(self, arr, N):
        # add code here
        
        x=0
        
        while True:
            
            y=max(arr)
            if y==0:
                return x
            print(y)
            x=max(x,x^y)
            arr=[min(z, z^y) for z in arr]
ob=Solution()
print(ob.maxSubarrayXOR([2,4,5],3))