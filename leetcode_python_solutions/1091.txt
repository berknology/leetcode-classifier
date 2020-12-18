class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        queue = collections.deque([(0, 0, 1)])
        while queue:
            i, j, step = queue.popleft()
            if (i, j) == (n-1, n-1): return step
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1), \
                (i+1, j+1), (i+1, j-1), (i-1, j-1), (i-1, j+1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append((x, y, step+1))
        return -1
