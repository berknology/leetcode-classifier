#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            ans = ans^i^num
        ans = ans^len(nums)
        return ans
        
# @lc code=end

