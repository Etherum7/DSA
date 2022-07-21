class Solution:
    def nCr(self, n, r):
        # code here
        t=[[1 if i==0 else 0   for i in range(r+1)]  for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, r+1):
                if j>i:
                    t[i][j]=0
                t[i][j]= t[i-1][j]+ t[i-1][j-1]
        return t[n][r]%(10**9 +7)