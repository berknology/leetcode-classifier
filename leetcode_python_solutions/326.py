class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        prod = 1
        while prod < n:
            prod *= 3
        return prod == n
        
