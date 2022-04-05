class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        return self.top_down(0, n, cuts, {})
    
    def top_down(self, left, right, cuts, memo):
        if (left, right) not in memo:
            ans = float('inf')
            for c in cuts:
                if left < c < right:
                    left_cut = self.top_down(left, c, cuts, memo)
                    right_cut = self.top_down(c, right, cuts, memo)
                    ans = min(ans, left_cut+right_cut+right-left)
            memo[(left, right)] = ans if ans != float('inf') else 0
        return memo[(left, right)]
        
        
"""
DP


"""
