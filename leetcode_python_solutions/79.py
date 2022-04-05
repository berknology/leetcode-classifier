class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.backtrack(board, word, 0, i, j):
                    return True
        return False
    
    def backtrack(self, board, word, index, i, j):
        if index == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index] or board[i][j] == None:
            return False
        temp = board[i][j]
        board[i][j] = None
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if self.backtrack(board, word, index+1, x, y):
                return True
        board[i][j] = temp
        return False
        
        
"""
backtracking


"""
