class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        return math.log(num, 4).is_integer()
        
