class Solution:
    def lcs(self, s1, s2, n, m):
        t = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return t[n][m]

    def length(self, s1, s2, n, m):
        return n+m - self.lcs(s1, s2, n, m)

    def minOperations(self, s1, s2):
        n = len(s1)
        m = len(s2)
        return m+n-2*self.lcs(s1, s2, n, m)

    def printShortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        t = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        i = n
        j = m
        res = ''
        while(i > 0 and j > 0):
            if str1[i-1] == str2[j-1]:
                res += str1[i-1]
                i -= 1
                j -= 1
            else:
                if t[i][j-1] > t[i-1][j]:
                    res += str2[j-1]
                    j -= 1
                else:
                    res += str1[i-1]
                    i -= 1
        while i > 0:
            res += str1[i-1]
            i -= 1
        while j > 0:
            res += str2[j-1]
            j -= 1
        return res[::-1]
