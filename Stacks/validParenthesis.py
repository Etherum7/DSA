class Solution:
    def valid(self, s):
        # code here
        st = []
        opn = ('(', '{', '[')
        # close=(')','}',']')
        for c in s:
            if c in opn:
                st.append(c)
            else:
                if not len(st):
                    return 0
                top = st.pop()
                if(top == '(' and c == ')') or (top == '{' and c == '}') or (top == '[' and c == ']'):
                    continue
                return 0
        if len(st):
            return 0
        return 1
