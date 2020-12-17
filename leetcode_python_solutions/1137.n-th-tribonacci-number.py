#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            dp = [0]*(n+1)
            dp[:3] = [0, 1, 1]
            for i in range(3, n+1):
                dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
            return dp[-1]
             
# @lc code=end

