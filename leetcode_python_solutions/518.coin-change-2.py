#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        return self._change(amount, coins, 0, {})
    
    def _change(self, amount, coins, index, memo):
        if index >= len(coins) or amount < 0:
            return 0
        if amount == 0:
            return 1
        if (index, amount) not in memo:
            include = self._change(amount-coins[index], coins, index, memo)
            not_include = self._change(amount, coins, index+1, memo)
            memo[(index, amount)] = include + not_include
        return memo[(index, amount)]


# @lc code=end

