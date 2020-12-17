#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1 or not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if i == 0:
                dp[i][0] = (1-obstacleGrid[i][0])
            else:
                dp[i][0] = (1-obstacleGrid[i][0])*dp[i-1][0]
        for j in range(n):
            if j == 0:
                dp[0][j] = (1-obstacleGrid[0][j])
            else:
                dp[0][j] = (1-obstacleGrid[0][j])*dp[0][j-1]       
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]


# @lc code=end

