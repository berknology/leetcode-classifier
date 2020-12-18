class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j**2] + 1)
        return dp[-1]
        

"""
dp[i] denotes the least number of perfect squares sum to i

for j in range(1, int(i**0.5)+1):
    dp[i] = min(dp[i], dp[i-j**2] + 1)

"""
