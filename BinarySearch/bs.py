# Recursive
class Solution:
    def binarysearch(self, arr, n, k):
        # code here
        def util(low, high):
            mid = (low+high)//2
            if low > high:
                return -1
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                return util(low, mid-1)
            else:
                return util(mid+1, high)
        return util(0, n-1)
def bS(arr,k):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            high=mid-1
        else:
            low=mid+1
    return -1
    