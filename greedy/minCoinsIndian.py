# User function Template for python3


class Solution:
    def minPartition(self, N):
        # code here
        coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]

        res = []
        i = 9
        while N > 0:
            if coins[i] > N:
                i -= 1
            else:
                res.append(coins[i])
                N -= coins[i]

        return res
