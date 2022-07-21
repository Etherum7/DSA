class Solution:
    def isBalanced(self, s):
        st = []
        for c in s:
            if c == '(':
                st.append(c)
            elif c == ')':
                if len(st):
                    st.pop()
                else:
                    return False
            else:
                continue
        if len(st):
            return False
        # print(s)
        return True

    def util(self, s, res, pos, op, n):

        if pos == n:
            # print(op)
            if self.isBalanced(op) and op not in res:
                
                res.append(op)
            return
        if pos > n:
            return

        if s[pos] == ')':
            self.util(s, res, pos+1,  op+')', n)
            self.util(s, res, pos+1,  op, n)
        elif s[pos] == '(':
            self.util(s, res, pos+1,  op+'(', n)
        else:
            self.util(s, res, pos+1, op+s[pos], n)

    def removeInvalidParentheses(self, s: str):
        res = []
        n = len(s)
        self.util(s, res, 0,  '', n)
        return res if len(res) else []


ob = Solution()
print(ob.removeInvalidParentheses('()())()'))
print(ob.removeInvalidParentheses('(a)())()'))
print(ob.removeInvalidParentheses(')('))
print(ob.removeInvalidParentheses('x('))
