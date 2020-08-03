class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ans = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        index = 0
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while len(ans) < m*n:
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x = i+direction[index][0]
            y = j+direction[index][1]
            if 0 <= x < m and 0 <= y < n and matrix[x][y]:
                i, j = x, y
            else:
                index = (index+1) % 4
                i = i+direction[index][0]
                j = j+direction[index][1]
        return ans


"""
Time complexity: O(mn), where m is the number of rows, n is the number of columns
Space complexity: O(1)
"""