#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i, num in enumerate(nums):
            if target - num  in hash_table:
                return [hash_table[target-num], i]
            hash_table[num] = i
        
# @lc code=end

