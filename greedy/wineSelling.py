class Solution:
    def wineSelling(self, A, N):
        # code here
        work = 0
        cur = 0
        for i in range(N):
            cur += A[i]
            work += abs(cur)
        return work
