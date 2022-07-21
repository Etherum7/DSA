from heapq import heappush, heappop, heapify


class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        heapify(A)
        res = 0
        for i in range(K1):
            heappop(A)

        for i in range(K2-K1-1):
            res += heappop(A)
        return res
