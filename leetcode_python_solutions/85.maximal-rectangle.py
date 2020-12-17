#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        self.ans = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0]*n
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j]+1 if matrix[i][j] == '1' else 0
            self.find_max_rectangle(heights[:])
        return self.ans
    
    def find_max_rectangle(self, heights):
        stack = [-1]
        heights.append(0)
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                cur_idx = stack.pop()
                h = heights[cur_idx]
                w = i - (stack[-1]+1)
                self.ans = max(self.ans, h*w)
            stack.append(i)
    
# @lc code=end

