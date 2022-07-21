class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        M = len(mat)
        N = len(mat[0])

        start = 0
        end = (M*N)-1

        while start <= end:
            mid = (start+end)//2
            if mat[mid//N][mid % N] == target:
                return True
            elif mat[mid//N][mid % N] > target:
                end = mid-1
            else:
                start = mid+1
        return False


class Solution:
    def searchMatrix(self, mat: List[List[int]], X: int) -> bool:
        N = len(mat)
        M = len(mat[0])
        startRow = 0
        endRow = N-1
        startCol = 0
        endCol = M-1
        while startRow <= endRow:
            midRow = (startRow+endRow)//2
            if midRow == N-1 or (mat[midRow][0] <= X and X < mat[midRow+1][0]):
                while startCol <= endCol:
                    midCol = (startCol+endCol)//2
                    if mat[midRow][midCol] == X:
                        return True
                    elif mat[midRow][midCol] > X:
                        endCol = midCol-1
                    else:
                        startCol = midCol+1
                return False

            elif X < mat[midRow][0]:
                endRow = midRow-1
            else:
                startRow = midRow+1
        return False
