# User function Template for python3
class Solution:
    def firstAndLast(self, arr, n, x):
        # Code here
        start = 0
        end = n-1
        resFirst = -1
        resLast = -1
        while start <= end:
            mid = (start+end)//2
            if arr[mid] == x:

                resFirst = mid
                end = mid-1

            elif arr[mid] > x:
                end = mid-1
            else:
                start = mid+1
        if resFirst == -1:
            return [-1]
        start = 0
        end = n-1

        while start <= end:
            mid = (start+end)//2
            if arr[mid] == x:

                resLast = mid
                start = mid+1

            elif arr[mid] > x:
                end = mid-1
            else:
                start = mid+1
        return [resFirst, resLast]
