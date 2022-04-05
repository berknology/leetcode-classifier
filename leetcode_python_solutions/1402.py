class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for j in range(n):
            if matrix[0][j] == 1:
                dp[0][j] = 1
        for i in range(m):
            if matrix[i][0] == 1:
                dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return sum([dp[i][j] for i in range(m) for j in range(n)])    
    

        
"""
DP

dp[i][j] represent the number of squares in the from top left (0, 0) to bottom right (i, j)

dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) if matrix[i][j] == 1
           0 

return dp[-1][-1]

"""
