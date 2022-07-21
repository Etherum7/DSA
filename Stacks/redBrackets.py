def findRedundant(s):
    st = []
    for c in s:
        if c != ')':
            st.append(c)
        else:
            flag = True
            if len(st):
                a = st.pop()
            else:
                return True
            while a != '(':
                if a in ['*', '+', '/', '-']:
                    flag = False
                if len(st):
                    a=st.pop()
                else:
                    break
            if flag:
                return True
    return False


Str = "((a+b))"
print(findRedundant(Str))

Str = "(a+(b)/c)"
print(findRedundant(Str))

Str = "(a+b*(c-d))"
print(findRedundant(Str))
