class Solution:
    def findKRotation(self, arr,  n):
        # code here
        start = 0
        end = n-1
        if arr[start] <= arr[end]:
            return 0
        while start <= end:
            mid = (start+end)//2
            prev = (mid+n-1) % n
            nex = (mid+1) % n
            if arr[mid] < arr[nex] and arr[mid] < arr[prev]:
                return mid
            elif arr[mid] < arr[end]:
                end = mid-1
            else:
                start = mid+1
