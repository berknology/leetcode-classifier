class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        hash_table = dict()
        index = 2
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j, index)
                    hash_table[index] = area
                    index += 1
        if not hash_table:
            return 1
        max_area = max(hash_table.values())
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] > 0:
                            neighbors.add(grid[x][y])
                    max_area = max(max_area, 1 + sum([hash_table[nei] for nei in neighbors]))
        return max_area
                
    def dfs(self, grid, i, j, index):
        area = 1
        grid[i][j] = index
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] == 1:
                area += self.dfs(grid, x, y, index)
        return area
        
        
"""
DFS

hash table

{
index: area

}


0,  1
1,  0

"""
