#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = left + (right-left)//2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left

# left    right   mid
# 1       5       3
# 4       5       4

# @lc code=end

