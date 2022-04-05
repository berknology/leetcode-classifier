class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, 'O', 'T')
            if board[i][n-1] == 'O':
                self.dfs(board, i, n-1, 'O', 'T')
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, 'O', 'T')
            if board[m-1][j] == 'O':
                self.dfs(board, m-1, j, 'O', 'T')
                
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    self.dfs(board, i, j, 'O', 'X')
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    self.dfs(board, i, j, 'T', 'O')
        
    def dfs(self, board, i, j, old, new):
        board[i][j] = new
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == old:
                self.dfs(board, x, y, old, new)
