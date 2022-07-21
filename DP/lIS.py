class Solution:
    def lcs(self, a, b, n, m):
        t=[[0] * (m+1) for j in range(n+1)]
        for i in range(1, n+1):
             for j in range(1, m+1):
                 if a[i-1]==b[j-1]:
                     t[i][j]=1+t[i-1][j-1]
                 else:
                     t[i][j]= max(t[i-1][j], t[i][j-1])
        return t[n][m]
        
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        b= sorted(set(a))
        return self.lcs(a, b , n, len(b))
    def longestSubsequence2(self,a,n):
        LIS=[1  for i in range(n+1)]
        for i in range(n):
            for j in range(i):
                if a[j]<a[i]:
                    LIS[i]= max(LIS[i], 1 + LIS[j])
        return max(LIS)