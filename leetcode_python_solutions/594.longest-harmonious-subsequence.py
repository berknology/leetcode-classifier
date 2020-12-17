#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        max_len = 0
        for num in counter.keys():
            if num+1 in counter:
                max_len = max(max_len, counter[num]+counter[num+1])
        return max_len
# @lc code=end

