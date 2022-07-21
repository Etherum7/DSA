# User function Template for python3
class Solution:

    def findMaximum(self, arr, n):
        # code here
        start = 0
        end = n-1
        if n == 1:
            return 0

        if arr[0] > arr[1]:
            return arr[0]
        if arr[n-1] > arr[n-2]:
            return arr[n-1]
        while start <= end:
            mid = (start+end)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return arr[mid]
            elif arr[mid-1] > arr[mid]:
                end = mid-1
            else:
                start = mid+1
