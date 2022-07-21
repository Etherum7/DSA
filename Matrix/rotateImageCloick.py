class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose

        for i in range(n):
            for j in range(i+1):
                t = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = t
        for i in range(n):
            start = 0
            end = n-1
            while start <= end:
                t = matrix[i][start]
                matrix[i][start] = matrix[i][end]
                matrix[i][end] = t
                start += 1
                end -= 1


# anti clockwise
class Solution:

    def rotateMatrix(self, matrix, n):
        # code here
        # transpose
        for i in range(n):
            for j in range(i+1):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        for i in range(n):
            start = 0
            end = n-1
            while start <= end:
                t = matrix[start][i]
                matrix[start][i] = matrix[end][i]
                matrix[end][i] = t
                start += 1
                end -= 1
