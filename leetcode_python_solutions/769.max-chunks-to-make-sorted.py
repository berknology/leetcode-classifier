#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        left_max = float('-inf')
        for i, num in enumerate(arr):
            left_max = max(left_max, num)
            if i >= left_max:
                ans += 1
        return ans

# @lc code=end

