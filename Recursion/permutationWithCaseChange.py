class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def util(ind, s, res, op):
            if ind == len(s):
                res.append(op)
                return
            if s[ind].isalpha():
                util(ind+1, s, res, op+s[ind].lower())
                util(ind+1, s, res, op+s[ind].upper())
            else:
                util(ind+1, s, res, op+s[ind])
        res = []
        util(0, s, res, '')
        return res
