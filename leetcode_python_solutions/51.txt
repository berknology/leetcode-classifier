class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        board = [['.']*n for _ in range(n)]
        self.backtrack(board, 0)
        return self.ans
    def backtrack(self, board, index):
        if index == len(board):
            self.ans.append([''.join(row) for row in board])
            return
        for j in range(len(board[0])):
            if self.is_safe(board, index, j):
                board[index][j] = 'Q'
                if self.backtrack(board, index+1):
                    return True
                board[index][j] = '.'
        return False
    
    def is_safe(self, board, i, j):
        for row in range(len(board)):
            if board[row][j] == 'Q':
                return False
            col1 = row+(j-i)
            if 0 <= col1 < len(board[0]) and board[row][col1] == 'Q':
                return False
            col2 = -row+(j+i)
            if 0 <= col2 < len(board[0]) and board[row][col2] == 'Q':
                return False
        return True
