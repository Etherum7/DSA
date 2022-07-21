class Solution:
    def maxSquare(self, n, m, mat):
        # code here
        t=[[0 for i in range(m+1)] for j in range(n+1)]
        max_till=0
        for i in range(1, n+1):
            for j in range(1,m+1):
                if mat[i-1][j-1]==0:
                    t[i][j]=0
            
                elif mat[i-1][j-1]==1 :
                    t[i][j]=min(t[i-1][j-1] , t[i-1][j], t[i][j-1] )+1
                
                if t[i][j]>max_till:
                    max_till=t[i][j]
        return max_till
                    
                