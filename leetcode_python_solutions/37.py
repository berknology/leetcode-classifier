class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        
    def find_first_unfilled(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    return i, j
        return -1, -1
    
    def solve(self, board):
        i, j = self.find_first_unfilled(board)
        if i == -1 and j == -1:
            return True
        for n in range(1, 10):
            if self.is_safe(board, i, j, str(n)):
                board[i][j] = str(n)
                if self.solve(board):
                    return True
                board[i][j] = '.'
        return False
    
    def is_row_safe(self, board, i, n):
        for j in range(len(board[0])):
            if board[i][j] == n:
                return False
        return True
        
    def is_col_safe(self, board, j, n):
        for i in range(len(board)):
            if board[i][j] == n:
                return False
        return True
    
    def is_cell_safe(self, board, i, j, n):
        i -= i%3 
        j -= j%3
        for row in range(i, i+3):
            for col in range(j, j+3):
                if board[row][col] == n:
                    return False
        return True
    
    def is_safe(self, board, i, j, n):
        return self.is_row_safe(board, i, n) and self.is_col_safe(board, j, n) and self.is_cell_safe(board, i, j, n)
    
