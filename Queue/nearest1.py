from queue import Queue


class Solution:
    def isValid(self, x, y, n, m):
        return x >= 0 and x < n and y >= 0 and y < m

    # Function to find distance of nearest 1 in the grid for each cell.
        def nearest(self, grid):
            # Code here
            q = Queue()
            n = len(grid)
            m = len(grid[0])
            ans = [[0]*m for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        q.put((i, j))
                        ans[i][j] = 0
                    else:
                        ans[i][j] = float('inf')
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            while not q.empty():
                p = q.get()
                for k in range(4):
                    new_x = dx[k]+p[0]
                    new_y = dy[k]+p[1]
                    if self.isValid(new_x, new_y, n, m) and ans[new_x][new_y] > ans[p[0]][p[1]]+1:
                        ans[new_x][new_y] = ans[p[0]][p[1]]+1
                        q.put((new_x, new_y))
            return ans
