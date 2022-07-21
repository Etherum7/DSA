class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        i = 0
        isNeg = False
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i < n and s[i] == '-':
            isNeg = True
            i += 1
        elif i < n and s[i] == '+':
            i += 1
        while i < n and 48 <= ord(s[i]) <= 57:
            if res == 0 and s[i] == '0':
                i += 1

            else:
                res = res*10+int(s[i])
                i += 1
        if isNeg:
            res = res*-1
        if res < -2147483648:
            res = -2147483648
        if res > 2147483647:
            res = 2147483647
        return res
