def generateBalancedParenthesis(n):
    def util(no, nc, op):
        if no < 0 or nc < 0:
            return
        if no == 0 and nc == 0 and op[-1] != '(':
            res.append(''.join(op))
            return
        if no == nc:
            op1 = op.copy()
            op1.append('(')
            util(no-1, nc, op1)
        else:
            op1 = op.copy()
            op2 = op.copy()
            op1.append('(')
            op2.append(')')
            util(no-1, nc, op1)
            util(no, nc-1, op2)
    res = []
    op = ['(']
    util(n-1, n, op)
    return res


print(generateBalancedParenthesis(2))
# User function Template for python3


class Solution:
    def AllParenthesis(self, n):
        # code here
        res = []

        def util(no, nc, op):
            if no < 0 or nc < 0:
                return
            if no == nc == 0:
                res.append(op)
                return
            if no > 0:
                util(no-1, nc, op+'(')
            if no < nc:
                util(no, nc-1, op+')')
        util(n-1, n, '(')
        return res
