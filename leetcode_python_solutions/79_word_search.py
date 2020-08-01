class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.backtrack(board, i, j, word):
                    return True
        return False

    def backtrack(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = None
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if self.backtrack(board, x, y, word[1:]):
                return True
        board[i][j] = temp
        return False
