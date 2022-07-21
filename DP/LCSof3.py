#User function Template for python3

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        t=[[[0 for i in range(n1+1)] for j in range(n2+1)] for k in range(n3+1)]
        for k in range(1,n3+1):
            for j in range(1,n2+1):
                for i in range(1, n1+1):
                    if A[i-1]==B[j-1]==C[k-1]:
                        t[k][j][i]=1+t[k-1][j-1][i-1]
                    else:
                        t[k][j][i]= max(t[k][j][i-1], t[k][j-1][i], t[k-1][j][i])
        return t[n3][n2][n1]