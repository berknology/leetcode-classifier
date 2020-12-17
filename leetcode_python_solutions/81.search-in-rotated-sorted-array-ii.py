#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            while nums[left] == nums[mid] == nums[right] and left < right:
                left += 1
                right -= 1
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        if nums[left] != target:
            return False
        return True


# @lc code=end

