def insert(stack, val):
    if len(stack) == 0 or stack[-1] < val:
        stack.append(val)
        return
    temp = stack.pop()
    insert(stack, val)
    stack.append(temp)


def sortStack(stack):
    # given data structure is a python list
    # as list have all the similar operations available so use them
    # Write your code here
    if len(stack) == 1:
        return
    val = stack.pop()
    sortStack(stack)
    insert(stack, val)
