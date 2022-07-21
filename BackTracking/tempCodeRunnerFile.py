class Solution:
    def util(self, s, n, nd, pos, res, op):

        if nd == 0:
            res.append(op)
            return
        # if pos >= n:
        #     return
        if pos < n-1:
            self.util(s, n, nd-1, pos+1, res, op[:pos]+'.'+op[pos:])
        if pos < n-1:
            self.util(s, n, nd, pos+1, res, op)
        return

    def genIp(self, s):
        # Code here
        n = len(s)
        if n < 4:
            return -1
        res = []
        self.util(s, n, 3, 1, res, s)
        return res


ob = Solution()
print(ob.genIp('1111'))
