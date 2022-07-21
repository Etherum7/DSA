# User function Template for python3
import sys
sys.setrecursionlimit(10**5)

class Solution:
    def isSafe(self, row, col, grid, visited):
        rowInBounds = 0 <= row < len(grid)
        colInBounds = 0 <= col < len(grid[0])
        if not rowInBounds or not colInBounds:
            return False
        if grid[row][col] == 0:
            return False
        if (row, col) in visited:
            return False
        return True

    def dfs(self, row, col, grid, visited):
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
        visited.add((row, col))
        for k in range(8):
            if self.isSafe(row + rowNbr[k], col + colNbr[k], grid, visited):
                self.dfs(row + rowNbr[k], col + colNbr[k], grid, visited)

    def numIslands(self, grid):
        # code here
        visited = set()
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] != 0:
                    self.dfs(row, col, grid, visited)
                    res += 1
        return res

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends
