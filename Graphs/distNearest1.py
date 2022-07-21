from curses.ascii import SO
from queue import Queue


class Solution:
    def isSafe(self, i, j, n, m, visited):
        if i >= 0 and i < n and j >= 0 and j < m and (i, j) not in visited:
            return True
        return False

    def bfs(self, a, b, grid):
        q = Queue()
        n = len(grid)
        m = len(grid[0])
        q.put((a, b, 0))
        visited = set()
        visited.add((a, b))
        while not q.empty():
            t = q.get()
            # print(t)
            i = t[0]
            j = t[1]
            if self.isSafe(i+1, j, n, m, visited):
                visited.add((i+1, j))
                print(i,j, t[2])
                if grid[i+1][j] == 1:
                    return t[2]+1
                else:
                    q.put((i+1, j, t[2]+1))
            if self.isSafe(i-1, j, n, m, visited):
                visited.add((i-1, j))
                if grid[i-1][j] == 1:
                    return t[2]+1
                else:
                    q.put((i-1, j, t[2]+1))
            if self.isSafe(i, j+1, n, m, visited):
                visited.add((i, j+1))
                if grid[i][j+1] == 1:
                    return t[2]+1
                else:
                    q.put((i, j+1, t[2]+1))
            if self.isSafe(i, j-1, n, m, visited):
                visited.add((i, j-1))
                if grid[i][j-1] == 1:
                    return t[2]+1
                else:
                    q.put((i, j-1, t[2]+1))

    def nearest(self, grid):
        # Code here
        n = len(grid)
        m = len(grid[0])
        res = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = self.bfs(i, j, grid)
        return res
ob=Solution()
print(ob.nearest([[0,1,1,0],[1,1,0,0],[0,0,1,1]]))
