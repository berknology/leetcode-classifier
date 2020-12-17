#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)

    def find_unfilled(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    return i, j
        return -1, -1

    def backtrack(self, board):
        i, j = self.find_unfilled(board)
        if (i, j) == (-1, -1):
            return True
        for num in range(1, 10):
            if self.is_safe(board, i, j, str(num)):
                board[i][j] = str(num)
                if self.backtrack(board):
                    return True
                board[i][j] = '.'
        return False
        
    def is_safe(self, board, i, j, num):
        is_col_safe = all([board[index][j] != num for index in range(len(board))])
        is_row_safe = all([board[i][index] != num for index in range(len(board[0]))])
        return is_col_safe and is_row_safe and self.is_cell_safe(board, i, j, num)

    def is_cell_safe(self, board, i, j, num):
        start_i = i - i%3
        start_j = j - j%3
        for row in range(3):
            for col in range(3):
                if board[start_i+row][start_j+col] == num:
                    return False
        return True

# @lc code=end

