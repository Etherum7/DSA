class Solution:
    def cutRod(self, price, n):
        l= [i for i in range(1,n+1)]
        t=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if l[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]= max(price[i-1]+ t[i][j-l[i-1]], t[i-1][j])
        return t[n][n]
        