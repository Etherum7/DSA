# User function Template for python3
from bisect import bisect_right


class Solution:
    def median(self, matrix, r, c):
        # code here
        start = float('inf')
        end = -float('inf')

        for i in range(r):
            start = min(start, matrix[i][0])
            end = max(end, matrix[i][c-1])
    # 	print(start,end)
        desired = ((r*c)+1)//2
        while start <= end:
            mid = (start+end)//2
            numOfLow = 0
            for row in range(r):
                numOfLow += bisect_right(matrix[row], mid)
            if numOfLow < desired:
                start = mid+1
            else:
                end = mid-1
        return start
