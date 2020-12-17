#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = collections.defaultdict(int)
        hash_table[0] = 1
        cum_sum = 0
        ans = 0
        for num in nums:
            cum_sum += num
            ans += hash_table[cum_sum-k]
            hash_table[cum_sum] += 1
        return ans

# @lc code=end

