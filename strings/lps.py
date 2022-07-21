# User function Template for python3

class Solution:
    def lps(self, s):
        # code here
        Len = 0
        n = len(s)
        lps = [0]*n
        maxTill = 0
        i = 1
        while i < n:
            if s[Len] == s[i]:
                Len += 1
                lps[i] = Len
                if Len > maxTill:
                    maxTill = Len
                i += 1
            else:
                if Len != 0:
                    Len = lps[Len-1]
                else:
                    lps[i] = 0
                    i += 1
        print(lps)
        return lps[n-1]
ob=Solution()
print(ob.lps('aacecaaaa'))