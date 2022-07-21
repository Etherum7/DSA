#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        if n<=1:
            return n
        arr.sort()
        dep.sort()
        plt=1
        maxPlt=1
        i=1
        j=0
        while i<n:
            
            while dep[j]<arr[i]:
                plt-=1
                j+=1
                
            if arr[i]<=dep[j]:
                plt+=1
                i+=1
                maxPlt=max(maxPlt, plt)
        return maxPlt