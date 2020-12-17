#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(len(nums)):
            length = 0
            idx = i
            while nums[idx] is not None:
                length += 1
                temp = nums[idx]
                nums[idx] = None
                idx = temp
            max_len = max(max_len, length)
        return max_len


# @lc code=end

