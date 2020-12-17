#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right-left)//2
            n = sum([bisect.bisect(row, mid) for row in matrix])
            if n < k:
                left = mid + 1
            else:
                right = mid
        return left
                
# @lc code=end

