class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = [-1]
        heights += [0]
        max_area = 0
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                index = stack.pop()
                h = heights[index]
                w = i - stack[-1] - 1
                max_area = max(max_area, h*w)
            stack.append(i)
        return max_area
        
        
"""
Monotone increasing stack

height[i]*(i-stack[-1]+1)
height[i]

[1,2]

[-1, 0, 1]

"""
