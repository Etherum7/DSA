def util(mat, i,j, m,n, res, op, ):
    rowInBounds=0<=i<m
    colInBounds=0<=j<n
    if not rowInBounds or not colInBounds:
        return 
    op.append(mat[i][j])
    if i==m-1 and j==n-1:
        # op.append(mat[i][j])
        res.append(op.copy())
        return
    util(mat, i+1, j, m,n, res, op.copy())
    util(mat, i, j+1, m, n, res, op.copy())
    return
    

def allPossiblePath(mat, m ,n):
    res=[]
    util(mat, 0,0, m,n, res, [])
    print(res)
mat = [[1, 2, 3],
       [4, 5, 6]]
maze = [[1,2,3],
            [4,5,6],
            [7,8,9]]
# allPossiblePath(mat, 2,3)
allPossiblePath(maze, 3,3)