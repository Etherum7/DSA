# User function Template for python3
class Solution:
    def setBits(self, N):
        c = 0

        while N:
            c += 1
            N = N & (N-1)
        return c
