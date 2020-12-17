#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) !=  len(B): return False
        return B in A+A

# @lc code=end

