#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        pac = [[False]*n for _ in range(m)]
        atl = [[False]*n for _ in range(m)]
        for i in range(m):
            self.dfs(matrix, i, 0, pac)
            self.dfs(matrix, i, n-1, atl)
        for j in range(n):
            self.dfs(matrix, 0, j, pac)
            self.dfs(matrix, m-1, j, atl)
        ans = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    ans.append([i, j])
        return ans
    
    def dfs(self, matrix, i, j, mat):
        mat[i][j] = True
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and not mat[x][y] and matrix[x][y] >= matrix[i][j]:
                self.dfs(matrix, x, y, mat)

# @lc code=end

