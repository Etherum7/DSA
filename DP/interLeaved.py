#User function Template for python3

 #Your task is to complete this Function \

class Solution:
    #function should return True/False
    def lcs(self, s1, s2, m, n):
        t=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[j-1]==s2[i-1]:
                    t[i][j]= 1+t[i-1][j-1]
                else:
                    t[i][j]= max(t[i-1][j], t[i][j-1])
        return t[n][m]
        
    def isInterleave(self, A, B, C):
        # Code here
        m=len(A)
        n=len(B)
        if len(C)!=m+n:
            return False
        
        t=[[False for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0:
                    t[i][j]=True
                elif i==0  and B[j-1]==C[j-1]:
                    t[i][j]=t[i][j-1]
                elif j==0 and A[i-1]==C[i-1]:
                    t[i][j]=t[i-1][j]
                else:
                    x=A[i-1]
                    y=B[j-1]
                    z=C[i+j-1]
                    if x==z and y!=z:
                        t[i][j]=t[i-1][j]
                    elif y==z and x!=z:
                        t[i][j]=t[i][j-1]
                    elif x==y==z:
                        t[i][j]=t[i-1][j] |t[i][j-1]
        return t[m][n]
        