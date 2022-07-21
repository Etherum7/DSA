from heapq import heappop, heappush


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        A.sort()
        B.sort()
        n = len(A)
        m = len(B)
        heap = []
        heappush(heap, (-(A[-1]+B[-1]), n-1, m-1))
        s = set()
        s.add((n-1, m-1))
        res = []
        for i in range(C):
            (val, u, v) = heappop(heap)
            res.append(-val)
            if (u-1, v) not in s:
                heappush(heap, (-(A[u-1]+B[v]), u-1, v))
                s.add((u-1, v))
            if (u, v-1) not in s:
                heappush(heap, (-(A[u]+B[v-1]), u, v-1))
                s.add((u, v-1))
        return res
