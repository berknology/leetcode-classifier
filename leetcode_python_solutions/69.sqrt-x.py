#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        left, right = 0, x
        while left < right:
            mid = left + (right-left)//2
            if mid*mid <= x:
                left = mid +1
            else:
                right = mid
        return left-1

# left    right   mid
# 0       8       4
# 0       4       2
# 3       4       3
# 3       3   

# @lc code=end

