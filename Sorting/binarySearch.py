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
