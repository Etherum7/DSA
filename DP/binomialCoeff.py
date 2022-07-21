class Solution:
    def nCr(self, n, r):
        # code here
        t=[[0  for i in range(r+1)]  for j in range(n+1)]
        for i in range( n+1):
            for j in range( r+1):
                if j==0 or j==i:
                    t[i][j]=1
                elif j>i:
                    t[i][j]=0
                else:
                    t[i][j]= t[i-1][j]+ t[i-1][j-1]
        print(t)
        return t[n][r]%(10**9 +7)
ob=Solution()
print(ob.nCr(3,2))