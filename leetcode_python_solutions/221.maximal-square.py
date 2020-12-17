#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        ans = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0]*(n+1)
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j]+1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for idx, height in enumerate(heights):
                while height < heights[stack[-1]]:
                    cur_idx = stack.pop()
                    h = heights[cur_idx]
                    w = idx - (stack[-1]+1)
                    ans = max(ans, min(h, w)**2)
                stack.append(idx)
        return ans

# @lc code=end

