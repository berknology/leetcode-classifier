#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for j in range(target+1):
            for num in nums:
                if j >= num:
                    dp[j] = dp[j] + dp[j-num]
        return dp[-1]

# @lc code=end

