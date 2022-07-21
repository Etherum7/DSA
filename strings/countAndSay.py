class Solution:
    def countAndSay(self, n: int) -> str:
        def next(a):
            i = 0
            res = []
            while i < len(a):
                count = 1
                while i+1 < len(s) and s[i] == s[i+1]:
                    count += 1
                    i += 1
                res.append(str(count) + s[i])
                i += 1
            return ''.join(res)

        s = '1'
        for _ in range(1, n):
            s = next(s)
        return s
