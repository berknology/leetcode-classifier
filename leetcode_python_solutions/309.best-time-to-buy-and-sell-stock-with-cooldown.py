#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        sold = [0]*(n+1)
        rest = [0]*(n+1)
        hold = [0]*(n+1)
        hold[0] = float('-inf')
        for i in range(1, n+1):
            sold[i] = hold[i-1]+prices[i-1]
            rest[i] = max(sold[i-1], rest[i-1])
            hold[i] = max(hold[i-1], rest[i-1]-prices[i-1])
        return max(sold[-1], rest[-1])

# @lc code=end

