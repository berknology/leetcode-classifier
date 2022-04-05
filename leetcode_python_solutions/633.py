class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5)+1):
            b_square = c - a**2
            if (int(b_square**0.5))**2 == b_square:
                return True
        return False
        
"""


"""
