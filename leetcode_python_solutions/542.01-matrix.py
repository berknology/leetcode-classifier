#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j, 0))
        ans = [[0]*n for _ in range(m)]
        while queue:
            i, j, step = queue.popleft()
            ans[i][j] = step
            for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1:
                    matrix[x][y] = 0
                    queue.append((x, y, step+1))
        return ans

# @lc code=end

