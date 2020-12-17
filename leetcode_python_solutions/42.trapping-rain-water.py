#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        ans = 0
        left, right = 0, len(height)-1
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                ans += left_max-height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                ans += right_max-height[right]
                right -= 1
        return ans

# @lc code=end

