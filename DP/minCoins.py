class Solution:
    def minCoins(self, coins, M, V):
        # code here
        t = [[100000 if j == 0 else 0 for i in range(V+1)] for j in range(M+1)]
        t[0][0] = 0
        for i in range(1, M+1):
            for j in range(1, V+1):
                if coins[i-1] > j:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = min(1 + t[i][j-coins[i-1]], t[i-1][j])
        if t[M][V] > V:
            return -1

        return t[M][V]
