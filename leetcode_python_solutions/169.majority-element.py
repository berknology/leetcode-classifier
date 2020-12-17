#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        hash_table = collections.defaultdict(int)
        for num in nums:
            hash_table[num] += 1
            if hash_table[num] > n:
                return num
        
# @lc code=end

