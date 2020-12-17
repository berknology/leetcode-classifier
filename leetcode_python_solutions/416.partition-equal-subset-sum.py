#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation%2 != 0:
            return False
        capacity = summation//2
        n = len(nums)
        dp = [[False]*(capacity+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            w = nums[i-1]
            for j in range(capacity+1):
                if j >= w:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


# dp[i][j] possible with the first i-1 items with weight equal to j
# dp[i][j] = dp[i-1][j] or dp[i-1][j-w]

# @lc code=end

