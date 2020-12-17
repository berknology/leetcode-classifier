#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1
        max_prod = float('-inf')
        for num in nums:
            cur_min, cur_max = min(num, cur_min*num, cur_max*num), max(num, cur_min*num, cur_max*num)
            max_prod = max(max_prod, cur_max)
        return max_prod
        

# max_prod        cur_min     cur_max
# float('-inf')       1           1
# 2                   2           2
# 6                   3           6
# 6                   -12         -2
# 6                   -48         4


# @lc code=end

