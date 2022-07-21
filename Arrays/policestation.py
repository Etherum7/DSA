# User function Template for python3

from typing import List


class Solution:
    def solve(self, N: int, a: int, x: List[int]) -> int:
        # code here
        max1 = -float('inf')
        max2 = -float('inf')
        val1 = abs(a-x[0])
        val2 = abs(a-x[1])
        max1 = val2
        max2 = val1
        if val1 > val2:
            max1 = val1
            max2 = val2

        for i in range(2, N):
            val = abs(a-x[i])
            if val > max2:
                if val > max1:
                    max2 = max1
                    max1 = val
                else:
                    max2 = val

        return max1+max2
