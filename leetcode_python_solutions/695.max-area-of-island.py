#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j, m, n))
        return ans

    def dfs(self, grid, i, j, m, n):
        area = 1
        grid[i][j] = 0
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                area += self.dfs(grid, x, y, m, n)
        return area

# @lc code=end

