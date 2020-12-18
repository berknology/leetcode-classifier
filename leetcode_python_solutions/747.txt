class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.top_down(cost, len(cost), {})
    
    def top_down(self, cost, index, memo):
        if index <= 1:
            return 0
        if index not in memo:
            ans = min(self.top_down(cost, index-2, memo) + cost[index-2], self.top_down(cost, index-1, memo) + cost[index-1])
            memo[index] = ans
        return memo[index]
  

        
"""
DP


"""
