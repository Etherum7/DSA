from typing import List


class Solution:
    def util(self, row, col, op, n, m, grid, res):

        if row == n-1 and col == m-1:
            op.append(grid[row][col])
            res.append(op)
            return

        op1 = op.copy()
        op2 = op.copy()

        op1.append(grid[row][col])
        op2.append(grid[row][col])

        if row < n-1:
            self.util(row+1, col, op1, n, m, grid, res)
        if col < m-1:
            self.util(row, col+1, op2, n, m, grid, res)
        return

    def findAllPossiblePaths(self, n: int, m: int, grid: List[List[int]]) -> List[List[int]]:
        # code here
        res = []
        self.util(0, 0, [], n, m, grid, res)
        return res


ob = Solution()
print(ob.findAllPossiblePaths(3, 3, [[1, 2, 3],
                                     [4, 5, 6],
                                     [7, 8, 9]]))
