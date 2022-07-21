class Solution:
    def LongestRepeatingSubsequence(self, s):
        # Code here
        n = len(s)
        t = [[0] * (n+1) for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s[j-1] and i != j:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return t[i][j]
