class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        prod = 0
        for num in nums:
            prod ^= num
        mask = 1
        while mask & prod == 0:
            mask <<= 1
        num1 = num2 = 0
        for num in nums:
            if num & mask != 0:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num
        return [num1, num2]
        
        
"""
bit manipulation
XOR

1 ^ 1 = 0
0 ^ 0 = 0
1 ^ 0 = 1
0 ^ 1 = 1

"""
