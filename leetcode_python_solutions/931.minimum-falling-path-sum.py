#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m = len(A)
        for i in range(1, m):
            for j in range(m):
                A[i][j] += min([A[i-1][k] for k in range(j-1, j+2) if 0 <= k < len(A[i-1])])
        return min(A[-1])


# @lc code=end

