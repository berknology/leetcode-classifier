class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = collections.deque([(i, j, 0) for i in range(n) for j in range(n) if grid[i][j] == 1])
        if len(queue) == 0 or len(queue) == n**2:
            return -1
        while queue:
            i, j, step = queue.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append((x, y, step+1))
        return step
