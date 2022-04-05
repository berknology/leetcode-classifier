class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0]*(n+1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.find_rect(heights))
        return ans
    
    def find_rect(self, heights):
        stack = [-1]
        ans = 0
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                index = stack.pop()
                h = heights[index]
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        return ans
        
