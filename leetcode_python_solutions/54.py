class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        i = j = 0
        for _ in range(m*n):
            element = matrix[i][j]
            ans.append(element)
            matrix[i][j] = None
            x = i + direction[d%4][0]
            y = j + direction[d%4][1]
            if x >= m or y >= n or matrix[x][y] == None:
                d += 1
            i += direction[d%4][0]
            j += direction[d%4][1]
        return ans

            
