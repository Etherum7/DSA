# User function Template for python3

class Solution:
    def search(self, A: list, l: int, h: int, key: int):
        # Complete this function

        start = l
        end = h
        while start <= end:
            mid = (start+end)//2

            if A[mid] == key:
                return mid
            elif A[start] <= A[mid]:
                if A[start] <= key and key <= A[mid]:
                    end = mid-1
                else:
                    start = mid+1

            else:
                if A[mid] <= key and key <= A[end]:
                    start = mid+1
                else:
                    end = mid-1
        return -1
