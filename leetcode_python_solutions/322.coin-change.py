#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1, n+1):
            w = coins[i-1]
            for j in range(1, amount+1):
                if j >= w:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-w]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

# dp[i][j] is the minimum number of coins from coins[:i] sum to j

# @lc code=end

