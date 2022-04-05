class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.top_down(amount, coins, 0, {})
    
    def top_down(self, amount, coins, index, memo):
        if amount == 0:
            return 1
        if index == len(coins):
            return 0
        if (amount, index) not in memo:
            coin = coins[index]
            if coin <= amount:
                include = self.top_down(amount-coin, coins, index, memo)
                not_include = self.top_down(amount, coins, index+1, memo)
                ans = include + not_include
            else:
                ans = self.top_down(amount, coins, index+1, memo)
            memo[(amount, index)] = ans
        return memo[(amount, index)]
    
