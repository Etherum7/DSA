class Solution:
    def __init__(self):
        self.t={}
    def convert(self, a,b):
        return a+' '+b
    def isScramble(self, s1, s2) :
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        if len(s1)<=1:
            return False
        key = self.convert(s1, s2)
        if key in self.t:
            return self.t[key]
        n= len(s1)
        flag=False
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]) or self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) ):
                flag=True
                break;
        self.t[key]=flag
        return flag
ob=Solution()
print(ob.isScramble('great', 'rgeat'))