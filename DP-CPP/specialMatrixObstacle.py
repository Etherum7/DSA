
class Solution:
    def FindWays(self, n, m, blocked_cells):
        # Code here
        mod = (10**9)+7
        blocked = set([tuple(x) for x in blocked_cells])
        if (n, m) in blocked:
            return 0
        dp = [0]*(m+1)
        temp = [0]*(m+1)
        for i in range(1, n+1):
            temp = [0]*(m+1)
            for j in range(1, m+1):
                # computinf gfor current
                if (i, j) in blocked:
                    temp[j] = 0
                elif i == 1 and j == 1:
                    temp[j] = 1
                else:
                    up = 0
                    left = 0
                    if i > 1:
                        up = dp[j]
                    if j > 1:
                        left = temp[j-1]
                    temp[j] = (up+left) % mod
            dp = temp
        return dp[m]
