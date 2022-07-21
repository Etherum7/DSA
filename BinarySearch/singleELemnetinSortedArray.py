#User function Template for python3
class Solution:
    def search(self, A, N):
        # your code here
        start=0
        end=N-2
        while start<=end:
            mid=(start+end)//2
            if mid%2==0:
                # even index
                if arr[mid]==arr[mid+1]:
                    start=mid+1
                else:
                    end=mid-1
            else:
                if arr[mid]==arr[mid+1]:
                    end=mid-1
                else:
                    start=mid+1
        return arr[start]
# XOR
# User function Template for python3
class Solution:
    def search(self, A, N):
        # your code here
        start = 0
        end = N-1
        if N == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[N-1] != arr[N-2]:
            return arr[N-1]

        while start <= end:
            mid = (start+end)//2

            if arr[mid] == arr[mid-1]:
                # right element
                # 2cases
                if mid % 2 == 0:
                    # right subarray
                    end = mid-1
                else:
                    start = mid+1

            elif arr[mid] == arr[mid+1]:
                # left element
                if mid % 2 == 0:
                    start = mid+1
                else:
                    end = mid-1
            else:
                return arr[mid]
