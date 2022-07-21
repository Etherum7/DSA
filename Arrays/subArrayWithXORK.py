from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        d = defaultdict(int)
        xr = 0
        for i in range(len(A)):
            xr = xr ^ A[i]
            if xr == B:
                count += 1
                # add
            if xr ^ B in d:
                count += d[xr ^ B]
            d[xr] += 1

        return count
# watch video