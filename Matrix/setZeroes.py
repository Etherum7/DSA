# 3 methods
# 1. set -1 when o by 4 while loops if not 0 then traverse and change -1 to 0
# 2. row and col array set 0 when 0 traverse if i in row 0 then set it to 0
# 3. use first row and col as row 0 to m and col 1to n thenforward pass set col row 0 when 0 set col0 =0 if first column ahas zero tracerse from reverse check if 0 then change also check if col0 is zero then col1=0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        
        col0=1
        for i in range(0, m):
            if matrix[i][0]==0:col0=0
            for j in range(1, n):
                
                if  matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if col0==0:
                matrix[i][0]=0
#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here
    m=len(matrix)
    n=len(matrix[0])
    cols=[1]*m
    rows=[1]*n
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                cols[i]=0
                rows[j]=0
    for i in range(m):
        for j in range(n):
            if rows[j]==0 or cols[i]==0:
                matrix[i][j]=1
    return matrix
