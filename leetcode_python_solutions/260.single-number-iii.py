#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        mask = xor&(-xor)
        num2 = 0
        num1 = 0
        for num in nums:
            if num&mask != 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]

# @lc code=end

