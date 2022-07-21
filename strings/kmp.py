def getLps(pat, m):
    lps = [0]*m
    i = 1
    Len = 0
    while i < m:
        if pat[i] == pat[Len]:
            Len += 1
            lps[i] = Len
            i += 1
        else:
            if Len != 0:
                Len = lps[Len-1]
            else:
                lps[i] = 0
                i += 1
    return lps


def findPattern(s: str, p: str):
    # Write your code here.
    n = len(s)
    m = len(p)
    lps = getLps(p, m)

    i = 0
    j = 0
    while i < n:
        if s[i] == p[j]:
            i += 1
            j += 1
        if j == m:
            return True
        elif i < n and s[i] != p[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return False
print(findPattern('cgfgfc','cfg' ))