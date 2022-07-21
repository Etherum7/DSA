

class Solution:
    def maxProfit(self,  N, A):
        # code here

        t = [[0 for i in range(N+1)] for j in range(3)]

        for i in range(1, 3):
            prevDiff = -float('inf')
            for j in range(1, N):
                prevDiff = max(prevDiff, t[i-1][j-1]-A[j-1])
                t[i][j] = max(t[i][j-1], A[j]+prevDiff)
        return t[2][N-1]


def stockBuySell(price, n):
    # code here
    if n == 1:
        return
    i = 0
    while i < n-1:
        while i < n-1 and price[i+1] <= price[i]:
            i += 1
        if i == n-1:
            return
        buy = i
        i += 1

        while i < n and price[i] >= price[i-1]:
            i += 1
        sell = i-1
        print (f"({buy} {sell})")
