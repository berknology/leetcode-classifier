#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        first_index = self.bisect_left(nums, target)
        if first_index == len(nums) or nums[first_index] != target:
            return [-1, -1]
        last_index = self.bisect(nums, target)
        return [first_index, last_index-1]
    
    def bisect_left(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid
        return left
    
    def bisect(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] <= target:
                left = mid +1
            else:
                right = mid
        return left

# @lc code=end

