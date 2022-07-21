# User function Template for python3

class Solution:
    def findEmptyLocation(self, grid, l):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    l[0] = row
                    l[1] = col
                    return True
        return False

    def usedInRow(self, grid, row, num):
        for x in range(9):
            if grid[row][x] == num:
                return True
        return False

    def usedInCol(self, grid, col, num):
        for x in range(9):
            if grid[x][col] == num:
                return True
        return False

    def usedInBox(self, grid, row, col, num):
        for i in range(3):
            for j in range(3):
                if grid[i+row][j+col] == num:
                    return True
        return False

    def isLocationSafe(self, grid, row, col, num):
        return not self.usedInRow(grid, row, num) and not self.usedInCol(grid, col, num) and not self.usedInBox(grid, row - row % 3, col-col % 3, num)
    # Function to find a solved Sudoku.

    def SolveSudoku(self, grid):
        l = [0, 0]
        if not self.findEmptyLocation(grid, l):
            return True
        row = l[0]
        col = l[1]

        for num in range(1, 10):
            if self.isLocationSafe(grid, row, col, num):
                grid[row][col] = num
                if self.SolveSudoku(grid):
                    return True
                grid[row][col] = 0
        return False
    # Function to print grids of the Sudoku.

    def printGrid(self, arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], sep=' ', end=' ')
