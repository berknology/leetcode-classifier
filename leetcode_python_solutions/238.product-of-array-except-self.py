#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prod = 1
        for i, num in enumerate(nums):
            ans[i] = prod
            prod = prod * num
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= prod
            prod = prod * nums[i]
        return ans

# @lc code=end

