#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = collections.defaultdict(int)
        for num in nums:
            hash_table[num] += 1
            if hash_table[num] > 1:
                return True
        return False

# @lc code=end

