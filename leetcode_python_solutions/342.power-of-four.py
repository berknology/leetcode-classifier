#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        return math.log(num, 4).is_integer()
        
# @lc code=end

