def maxSubstring( S):
    # code here
    n = len(S)
    t = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if S[i-1] == '0':
            if t[i-1] == -1:
                t[i] = 1
            else:
                t[i] = t[i-1]+1
        elif S[i-1]=='1':
            if t[i-1] == -1:
                t[i] = -1
            else:
                t[i] = t[i-1]-1
    print(t)

    return max(t[1:])
print(maxSubstring('11000010001'))