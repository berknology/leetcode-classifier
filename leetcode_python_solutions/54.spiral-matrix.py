#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        index = 0
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while len(ans) < m*n:
            ans.append(matrix[i][j])
            if i+dir[index][0] < 0 or i+dir[index][0] >= m or j+dir[index][1] < 0  or j+dir[index][1] >= n:
                index += 1
                index = index%4
        return ans

# @lc code=end

