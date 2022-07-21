class Solution:
    def isValid(self,val, board, row, col):
        for i in range(9):
            if board[i][col]==val:
                return False
            if board[row][i]==val:
                return False
        for r in range(row-row%3, (row-row%3)+3):
            for c in range(col-col%3, (col-col%3)+3):
                if board[r][c]==val:
                    return False
        return True
        
    def util(self, board, n):
        for i in range(n):
            for j in range(n):
                if board[i][j]=='.':
                    for c in range(1, 10):
                        if self.isValid(str(c),board, i, j):
                            board[i][j]=str(c)
                            if self.util(board,n):
                                return True
                            board[i][j]='.'
                    return False
        return True
                            
                        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if self.util(board, len(board)):
            return board
        
        