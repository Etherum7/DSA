# User function Template for python3

class Solution:
    def search(self, patt, s):
        # code here
        # No of charecter
        d = 256
        res = []
        # Prime
        q = 101
        # hash of pat
        p = 0
        # text
        m = len(patt)
        n = len(s)
        h = (d**(m-1)) % q
        t = 0
        for i in range(m):
            p = (d*p + ord(patt[i])) % q
            t = (d*t + ord(s[i])) % q

        for i in range(n-m+1):
            if p == t:
                for j in range(m):
                    if s[i+j] != patt[j]:
                        break
                if j == m-1 and s[i+j] == patt[j]:
                    res.append(i+1)
            if i < n-m:
                t = (d*(t-ord(s[i])*h)+ord(s[i+m])) % q

        return [-1] if len(res) == 0 else res
