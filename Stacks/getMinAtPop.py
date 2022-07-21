cur_min = 0


def _push(a, n):
    global cur_min
    cur_min = a[0]
    st = [a[0]]
    for ele in a[1:]:
        if ele >= cur_min:
            st.append(ele)
        else:

            st.append(2*ele-cur_min)
            cur_min = ele
    return st

# Function to print minimum value in stack each time while popping.


def _getMinAtPop(stack):
    global cur_min
    while (len(stack)):
        print(cur_min, end=' ')
        if stack[-1] < cur_min:
            cur_min = 2*cur_min-stack[-1]
        stack.pop()
