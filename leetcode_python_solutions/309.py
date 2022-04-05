class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sold = [0]*(n+1)
        hold = [0]*(n+1)
        hold[0] = float('-inf')
        rest = [0]*(n+1)
        for i, price in enumerate(prices):
            sold[i+1] = hold[i]+price
            rest[i+1] = max(rest[i], sold[i])
            hold[i+1] = max(rest[i]-price, hold[i])
        return max(rest[-1], sold[-1])
        
            
"""  
      cooldown
sold  ->  rest
      buy
rest  -> hold
     cooldown
rest  -> rest
         
     cooldown
hold  -> hold
     sell
hold  -> sold

"""


