#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if abs(_sum - target) < diff:
                    diff = abs(_sum - target)
                    ans = _sum
                if _sum == target:
                    return _sum
                elif _sum < target:
                    left += 1
                else:
                    right -= 1
        return ans
# @lc code=end

