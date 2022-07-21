def noOfSpanningTree(M, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i][j] = sum(M[i])
    for i in range(n):
        for j in range(n):
            if i != j and M[i][j]==1:
                M[i][j] = -1

    # print(M)
    cofMat = getCoFactor(M, 0, 0)
    # print(cofMat)
    return cofactor(cofMat)


def getCoFactor(M, i, j):
    return [row[:j]+row[j+1:] for row in (M[:i]+M[i+1:])]


def cofactor(M):
    if len(M) == 2:
        # print(M)
        return M[0][0]*M[1][1]-M[1][0]*M[0][1]
    res = 0
    for col in range(len(M)):
        sign = (-1) **col
        # print(sign, col)
        cof = cofactor(getCoFactor(M, 0, col))
        res += sign * M[0][col]*cof
        # print(res)
    return res


mat = [[0, 0, 1, 1],
       [0, 0, 1, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 0]]

print(noOfSpanningTree(mat, 4))
