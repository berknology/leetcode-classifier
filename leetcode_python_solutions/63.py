class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for j in range(1, n):
            dp[0][j] = (1-obstacleGrid[0][j])*dp[0][j-1]
        for i in range(1, m):
            dp[i][0] = (1-obstacleGrid[i][0])*dp[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] == 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

            
"""
dp[i][j] denotes the number of paths from (0, 0) to (i, j)
        
dp[i][j] = dp[i-1][j] + dp[i][j-1], if obtacleGrid[i][j] == 0
           0                      ,  else

the answer is dp[-1][-1]
"""

