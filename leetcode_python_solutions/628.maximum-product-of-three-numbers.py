#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        max3, max2, max1 = tuple(sorted(nums[:3]))
        min1, min2, _ = tuple(sorted(nums[:3]))
        for i in range(3, len(nums)):
            num = nums[i]
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num
            elif num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
        return max(max1*max2*max3, max1*min2*min1)

# @lc code=end

