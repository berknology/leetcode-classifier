class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_area = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0]*(n+1)
        for i in range(m):
            for j in range(n):
                heights[j] = 1+heights[j] if matrix[i][j] == '1' else 0
            max_area = max(max_area, self.find_square(heights))
        return max_area
    
    def find_square(self, heights):
        stack = [-1]
        max_square = 0
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                index = stack.pop()
                h = heights[index]
                w = i - stack[-1] - 1
                max_square = max(max_square, min(h, w)**2)
            stack.append(i)
        return max_square

    
