# User function Template for python3
class Solution:

    def perfectSum(self, arr, n, sum):
        # code here
        t = [[1 if i == 0 and j == 0 else 0 for i in range(
            sum+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(0, sum+1):
                if arr[i-1] > j:
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
        return (t[n][sum] % (10**9 + 7))
