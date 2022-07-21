class Solution:
    # Function to find the length of longest common subsequence in two strings.
    def lcs(self, x, y, s1, s2):
        t = [[0 for i in range(y+1)] for j in range(x+1)]
        for i in range(1, x+1):
            for j in range(1, y+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return t[x][y]

    def printLcs(self,x, y, s1, s2):
        res = ''
        t = [[0 for i in range(y+1)] for j in range(x+1)]
        for i in range(1, x+1):
            for j in range(1, y+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                    
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        i=x
        j=y
        while t[i][j]>0:
            if s1[i-1]==s2[j-1]:
                res+=s1[i-1]
                i-=1
                j-=1
            else:
                if t[i-1][j]> t[i][j-1]:
                    i-=1
                else:
                    j-=1
        return res[::-1]
x=6
y=7
s1='AGGTAB'
s2='GXTXAYB'


ob=Solution()
print(ob.printLcs(x, y, s1, s2))