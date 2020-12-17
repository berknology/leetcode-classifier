#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if (sum(nums)+S)%2 != 0 or sum(nums) < S:
            return 0
        capacity = (sum(nums)+S)//2
        n = len(nums)
        dp = [[0]*(capacity+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            w = nums[i-1]
            for j in range(capacity+1):
                if j >= w:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-w]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

# dp[i][j] denotes the number of ways to fit the first i-1 items with capapcity j

# @lc code=end

