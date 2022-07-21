class Solution:
    def isSafe(self, pos, n, grid, visited):
        return pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < n and grid[pos[0]][pos[1]] != 0 and not visited[pos[0]][pos[1]]

    def traverse(self, pos, grid, visited):
        visited[pos[0]][pos[1]] = True
        x = [0, 1, -1, 0]
        y = [1, 0, 0, -1]
        if grid[pos[0]][pos[1]] == 2:
            return True
        for k in range(4):
            if self.isSafe((pos[0]+x[k], pos[1]+y[k]), n, grid, visited):
                if self.traverse((pos[0]+x[k], pos[1]+y[k]), grid, visited):
                    return True
        return False

    # Function to find whether a path exists from the source to destination.

        def is_Possible(self, grid):
            # Code here
            n = len(grid)
            visited = [[False]*n for _ in range(n)]

            src = (0, 0)
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        src = (i, j)
                        break
            return self.traverse(src, grid, visited)
