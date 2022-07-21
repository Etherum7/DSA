# from math import ceil

# learb euclid solution
# use ceil
#User function Template for python3
import math
class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        gap=math.ceil((n+m)/2)
        # gap=(n+m)//2
        
        while gap>0:
            i=0
            j=gap
            while j<n+m:
                if j<n and arr1[i]>arr1[j]:
                    # first array
                    arr1[i],arr1[j]=arr1[j],arr1[i]
                elif j>=n and i<n and arr1[i]>arr2[j-n]:
                    arr1[i],arr2[j-n]=arr2[j-n],arr1[i]
                elif j>=n and i>=n and arr2[i-n]>arr2[j-n]:
                    arr2[i-n],arr2[j-n]=arr2[j-n],arr2[i-n]
                i+=1
                j+=1
            # gap=gap//2
            if gap==1:
                gap=0
            else:
                gap=math.ceil(gap/2)