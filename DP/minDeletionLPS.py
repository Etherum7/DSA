
class Solution:
    def lcs(self, s1, s2, n, m):
        t=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1, n+1):
             for j in range(1, m+1):
                  if s1[i-1]==s2[j-1]:
                      t[i][j]= 1+t[i-1][j-1]
                  else:
                      t[i][j]=max(t[i-1][j], t[i][j-1])
        return t[n][m]
                
    def longestPalinSubseq(self, S):
        n= len(S)
        return self.lcs(S, S[::-1], n, n)