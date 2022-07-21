from queue import Queue

from typing import List
import sys
sys.setrecursionlimit(10**5)


class Solution:
    def isSafe(self, pos, n, m, visited, mat):
        return pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < m and mat[pos[0]][pos[1]] != 0 and (pos[0], pos[1]) not in visited

    def util(self, start, end, mat, visited, n, m, res, d):
        visited.add((start[0], start[1]))
        if start[0] == end[0] and start[1] == end[1]:
            if res[0] < d:
                res[0] = d
                visited.remove((start[0], start[1]))
                return
        path = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for p in path:
            if self.isSafe((start[0]+p[0], start[1]+p[1]), n, m, visited, mat):
                self.util((start[0]+p[0], start[1]+p[1]),
                          end, mat, visited, n, m, res, d+1)
        visited.remove((start[0], start[1]))
        return

    def longestPath(self, mat: List[List[int]], n: int, m: int, xs: int, ys: int, xd: int, yd: int) -> int:
        # code here
        visited = set()
        visited.add((xs, ys))
        # q=Queue()
        res = [0]
        # q.put((xs,ys,0))
        self.util((xs, ys), (xd, yd), mat, visited, n, m, res, 0)
        if res[0] != 0:
            return res[0]
        return -1


ob = Solution()
mat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
mat2 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1]
]
print(ob.longestPath(mat, 3, 10, 0, 0, 0, 7))
print(ob.longestPath(mat2, 6, 4, 3, 2, 3, 1))
