def util(index, s, n, dictionary, res, op, sop):
    # print(op)
    if len(op) > 0 and op[-1] not in dictionary:
        return
    
    if sop==s:
        print(op)
        res.append(' '.join(op))
        return
    if index > n:
        return
    for i in range(index, n):
        op1 = op.copy()
        op1.append(s[index:i+1])
        sop1 = sop+s[index:i+1]
        util(i+1, s, n, dictionary, res, op1, sop1)


def wordBreak(s, dictionary):
    res = []
    util(0, s, len(s), dictionary, res, [], '')
    return res


print(wordBreak(
    'godisnowherenowhere', set(['god', 'is', 'now', 'no', 'where', 'here'])))
