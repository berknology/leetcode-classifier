#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        pre, cur = 1, 2
        for _ in range(2, n):
            pre, cur = cur, cur+pre 
        return cur

# dp[i] = dp[i-1] + dp[i-2]
#            cur      pre
# @lc code=end

