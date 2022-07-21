class Solution:
    def minDifference(self, arr, n):
        r = sum(arr)
        maxHalf = self.knapsack(arr, arr, n, r//2)
        return r-2*maxHalf

    def knapsack(self, wt, val, n, W):
        t = [[0 for i in range(W+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, W+1):
                if wt[i-1] > j:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = max(val[i-1] + t[i-1][j-val[i-1]], t[i-1][j])
        return t[n][W]
