# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        start=0
        end=n-1
        if n==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[n-1]>arr[n-2]:
            return n-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid]:
                end=mid-1
            else:
                start=mid+1