# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        t=[[0 for i in range(m+1)] for j in range(n+1)]
        for col in range(m-1 , -1, -1):
            for row in range(n):
                if col==m-1:
                    right=0
                else:
                    right= t[row][col+1]
                if row==0 or col==m-1:
                    rightUp=0
                else:
                    rightUp=t[row-1][col+1]
                if row==n-1 or col==m-1:
                    rightDown=0
                else:
                    rightDown=t[row+1][col+1]
                t[row][col]= M[row][col]+ max(right, rightUp, rightDown)
        res=0
        for i in range(n+1):
            res=max(res, t[i][0])
        return res
                    
                    
                    
                