#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return max(nums)
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

    def _rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return max(nums)
        else:
            nums[1] = max(nums[:2])
            for i in range(2, n):
                nums[i] = max(nums[i-1], nums[i-2]+nums[i])
            return nums[-1]
# @lc code=end

