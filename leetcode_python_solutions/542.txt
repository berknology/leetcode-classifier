class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[0]*n for _ in range(m)]
        queue = collections.deque([(i, j, 0) for i in range(m) for j in range(n) if matrix[i][j] == 0])
        while queue:
            i, j, step = queue.popleft()
            ans[i][j] = step
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1:
                    matrix[x][y] = 0
                    queue.append((x, y, step+1))
        return ans
        
        
"""
BFS



"""
