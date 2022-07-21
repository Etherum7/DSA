
class Solution:

    def optimalStrategyOfGame(self, arr, n):
        # code here
        dp = [[0 for i in range(n)] for j in range(n)]
        for gap in range(n):
            for j in range(gap, n):
                i = j-gap
                x = y = z = 0
                if i+2 <= j:
                    x = dp[i+2][j]
                if i+1 <= j-1:
                    y = dp[i+1][j-1]
                if i <= j-2:
                    z = dp[i][j-2]
                dp[i][j] = max(arr[i]+min(x, y), arr[j]+min(y, z))
        return dp[0][n-1]
