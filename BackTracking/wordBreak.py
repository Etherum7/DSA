from itertools import groupby
class Solution:
    def wordBreak(self, n, d, s):
        # code here
        res = []

        def util(pos, ip, op):
            if len(op) > 0 and op[-1] not in d:
                return
            if ''.join(op) == s:
                res.append(op.copy())
                return
            if pos <= len(ip):
                ip1 = ip[pos+1:]
                ip2 = ip
                op1 = op.copy()
                op2 = op.copy()
                op1.append(ip[:pos+1])

                util(0, ip1, op1)
                util(pos+1, ip2, op2)
            return

        util(0, s, [])
        res=list(k for k,_ in groupby(res))

        return res


ob = Solution()
print(ob.wordBreak(5, {"cats", "cat", "and", "sand", "dog"}, 'catsanddog'))
