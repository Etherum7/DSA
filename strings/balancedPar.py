class Solution:
    def find_permutation(self, S):
        # Code here
        res = []
        n = len(S)

        def util(op, remaining):
            if len(op) == n:
                res.append(op)
                return
            for i in remaining:
                t = remaining.copy()
                t.remove(i)
                util(op+i, t)
        ip = list(S)
        util('', ip)
        return sorted(res)
