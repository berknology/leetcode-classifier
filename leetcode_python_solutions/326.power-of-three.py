#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        prod = 1
        while prod < n:
            prod *= 3
        return prod == n
        
# @lc code=end

