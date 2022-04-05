class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        pre, cur = 1, 2
        for _ in range(2, n):
            pre, cur = cur, cur+pre 
        return cur
