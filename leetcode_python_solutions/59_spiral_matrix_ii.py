class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        index = 0
        i, j = 0, 0
        for num in range(n**2):
            ans[i][j] = num+1
            x, y = i+direction[index][0], j+direction[index][1]
            if 0 <= x < n and 0 <= y < n and ans[x][y] == 0:
                i, j = x, y
            else:
                index = (index+1) % 4
                i, j = i+direction[index][0], j+direction[index][1]
        return ans


"""
Time complexity: O(n^2), where m is the number of rows, n is the number of columns
Space complexity: O(n^2)
"""
