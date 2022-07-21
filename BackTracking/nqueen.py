class Solution:
    def isSafe(self, row, col, n, hashDigLow, hashDigUp, hashRow):
        if hashRow[row] == 1:
            return False
        if hashDigLow[row+col] == 1:
            return False
        if hashDigUp[(n-1)+(col-row)] == 1:
            return False
        return True

    def util(self, col, board, n, res, hashDigLow, hashDigUp, hashRow):
        if col == n:
            res.append([''.join(x) for x in board])
            return
        for row in range(n):
            if self.isSafe(row, col, n,  hashDigLow, hashDigUp, hashRow):
                board[row][col] = 'Q'
                hashRow[row] = 1
                hashDigLow[row+col] = 1
                hashDigUp[(n-1)+(col-row)] = 1
                self.util(col+1, board, n, res,
                          hashDigLow, hashDigUp, hashRow)
                board[row][col] = '.'
                hashRow[row] = 0
                hashDigLow[row+col] = 0
                hashDigUp[(n-1)+(col-row)] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for _ in range(n)]
        hashDigLow = [0]*((2*n)-1)
        hashDigUp = [0]*((2*n)-1)
        hashRow = [0]*n
        self.util(0, board, n, res, hashDigLow, hashDigUp, hashRow)
        return res


class Solution:
    def nQueen(self, n):
        # code here
        remaining = [1]*n
        res = []

        def util(op, remaining):
            # check criteria
            if len(op) > 1:
                for i in range(len(op)-1):
                    if abs(op[-1]-op[i]) == abs(len(op)-1 - i):
                        return
            if not 1 in remaining:

                res.append(op.copy())
                return
            for index, val in enumerate(remaining):
                tempRem = remaining.copy()
                if val == 1:
                    op1 = op.copy()
                    op1.append(index+1)
                    tempRem[index] = 0
                    util(op1, tempRem)
        util([], remaining)
        return res


ob = Solution()
print(ob.nQueen(4))


class Solution:
    def isSafe(self, row, col, board, n):
        dupRow = row
        dupCol = col
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
            row -= 1
        col = dupCol
        row = dupRow
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
        row = dupRow
        col = dupCol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1

        return True

    def util(self, col, board, n, res):
        if col == n:
            res.append([''.join(x) for x in board])
            return
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col] = 'Q'
                self.util(col+1, board, n, res)
                board[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for _ in range(n)]
        self.util(0, board, n, res)
        return res
