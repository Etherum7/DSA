class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        i=0
        j=0
        k=n-1
        while i<=k and j<m:
            if arr1[i]<arr2[j]:
                i+=1
            else:
                arr1[k],arr2[j]=arr2[j],arr1[k]
                j+=1
                k-=1
        arr1.sort()
        arr2.sort()

class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        i=0
        while arr1[n-1]>arr2[0]:
            if arr1[i]>arr2[0]:
                arr1[i],arr2[0]=arr2[0],arr1[i]
                # sort arr 2
                j=1
                
                while j<m and arr2[j]<arr2[j-1]:
                    arr2[j-1],arr2[j]=arr2[j],arr2[j-1]
                    j+=1
            i+=1