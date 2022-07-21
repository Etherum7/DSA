class Solution:
    def graycode(self, n):
        # code here
        if n == 1:
            return ['0', '1']
        l1 = self.graycode(n-1)
        l2 = reversed(l1)
        modl1 = ['0'+i for i in l1]
        modl2 = ['1'+i for i in l2]
        return modl1+modl2
