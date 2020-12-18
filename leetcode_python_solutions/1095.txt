class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[1]-x[0]), reverse=True)
        ans = 0
        n_a = 0
        n_b = 0
        n = len(costs)//2
        for i in range(2*n):
            if (n_a < n and costs[i][0] <= costs[i][1]) or n_b == n:
                n_a += 1
                ans += costs[i][0]
            else:
                n_b += 1
                ans += costs[i][1]
        return ans
        
        
        
"""
sort cost by the absolute different cost a and cost b

"""
