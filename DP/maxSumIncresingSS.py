class Solution:
    def maxSumIS(self, A, n):
        # code here
        t = A.copy()
        for i in range(1, n):
            for j in range(i+1):
                if A[j] < A[i]:
                    t[i] = max(t[i], t[j]+A[i])
        return max(t)
