#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_len = 1
                while num + 1 in nums_set:
                    cur_len += 1
                    num += 1
                max_len = max(max_len, cur_len)
        return max_len

# @lc code=end

