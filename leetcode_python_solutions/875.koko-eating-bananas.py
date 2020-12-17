#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2
            if not self.is_feasible(piles, mid, H):
                left = mid + 1
            else:
                right = mid
        return left

    def is_feasible(self, piles, mid, H):
        ans = 0
        for pile in piles:
            ans += (pile//mid) + (pile%mid > 0)
        return ans <= H

# @lc code=end

