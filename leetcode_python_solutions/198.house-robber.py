#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        self.nums = nums
        return self._rob(n-1)

    @lru_cache
    def _rob(self, index):
        if index == 0:
            return self.nums[0]
        elif index == 1:
            return max(self.nums[:2])
        return max(self._rob(index-1), self._rob(index-2)+self.nums[index])


# dp[i] = max(dp[i-1], dp[i-2]+nums[i])

# @lc code=end

