class Solution:
    def __init__(self):
        self.t=[[-1 for i in range(y+1)] for j in range(x+1)]
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        if x==0 or y==0:
            return 0
        if self.t[x][y]!=-1:
            return self.t[x][y]
        if s1[x-1] ==s2[y-1]:
            self.t[x][y]=1 + self.lcs(x-1, y-1, s1, s2)
            return self.t[x][y]
        else:
            self.t[x][y]=max(self.lcs(x-1, y, s1, s2), self.lcs(x, y-1, s1, s2))
            return self.t[x][y]
x=6
y=6
s1='ABCDGH'
s2='AEDFHR'


ob=Solution()
print(ob.lcs(x, y, s1, s2))
