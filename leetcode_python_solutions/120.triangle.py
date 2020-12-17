#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min([triangle[i-1][k] for k in range(j-1, j+1) if 0 <= k < len(triangle[i-1])])
        return min(triangle[-1])

# @lc code=end

