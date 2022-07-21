
class Solution:
    def romanToDecimal(self, S):
        # code here
        n = len(S)

        mp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = mp[S[-1]]
        for i in range(n-2, -1, -1):
            if mp[S[i]] < mp[S[i+1]]:
                res = res-mp[S[i]]
            else:
                res = res+mp[S[i]]
        return res
