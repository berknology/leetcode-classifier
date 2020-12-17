#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        self.hash_table = dict()
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j, index)
                    self.hash_table[index] = area
                    index += 1
        if len(self.hash_table) == 0: return 1
        max_area = max(self.hash_table.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] > 0:
                            neighbors.add(grid[x][y])
                    max_area = max(max_area, 1 + sum([self.hash_table[nei] for nei in neighbors]))
        return max_area
    
    def dfs(self, grid, i, j, index):
        area = 1
        grid[i][j] = index
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                area += self.dfs(grid, x, y, index)
        return area

# @lc code=end

