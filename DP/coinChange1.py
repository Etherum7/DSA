class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        t=[[ 1 if i==0 else 0 for i in range(amount+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1]> amount:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i][j-coins[i-1]] + t[i-1][j]
        return t[n][amount]