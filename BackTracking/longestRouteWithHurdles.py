R = 7
C = 4


def util(mat, i, j, x, y, d, visited, res):
    rowInBounds = 0 <= i <= R
    colInBounds = 0 <= j <= C
    if not rowInBounds or not colInBounds or mat[i][j] == 0 or visited[i][j]:
        return
    visited[i][j] = True

    if i == x and j == y and d > res[0]:
        res[0] = d
        visited[i][j] = False
        return

    if i < R-1 and not visited[i+1][j]:
        util(mat, i+1, j, x, y, d+1, visited, res)
    if j < C-1 and not visited[i][j+1]:
        util(mat, i, j+1, x, y, d+1, visited, res)
    if i > 0 and not visited[i-1][j]:
        util(mat, i-1, j, x, y, d+1, visited, res)
    if j > 0 and not visited[i][j-1]:
        util(mat, i, j-1, x, y, d+1, visited, res)
    visited[i][j] = False
    return


def longestRoute(mat, i, j, x, y):
    visited = []
    for _ in range(R):
        visited.append([])
        for _q in range(C):
            visited[-1].append(False)

    res = [0]
    if mat[i][j] == 0 or mat[x][y] == 0:
        return 0
    util(mat, i, j, x, y, 0, visited, res)
    return res[0]


mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# print(longestRoute(mat, 0, 0, 1, 7))
mat2 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1]
]
mat3 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 1]]
print(longestRoute(mat3, 3, 2, 4, 0))
