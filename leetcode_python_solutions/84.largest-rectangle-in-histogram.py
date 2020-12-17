#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        max_area = 0
        for idx, height in enumerate(heights):
            while height < heights[stack[-1]]:
                cur_idx = stack.pop()
                h = heights[cur_idx]
                max_area = max(max_area, h*(idx-(stack[-1]+1)))
            stack.append(idx)
        return max_area


# @lc code=end

