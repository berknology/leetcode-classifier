#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        hash_table = collections.defaultdict(int)
        _min, _max = float('inf'), float('-inf')
        for num in nums:
            _min = min(_min, num)
            _max = max(_max, num)
            hash_table[num] += 1
        if len(hash_table) == 1:
            return hash_table[_min]*_min
        dp = [0]*(_max-_min+1)
        dp[0] = hash_table[_min]*_min
        dp[1] = max(dp[0], hash_table[_min+1]*(_min+1))
        for i in range(2, _max-_min+1):
            dp[i] = max(dp[i-2]+hash_table[i+_min]*(i+_min), dp[i-1])
        return dp[-1]



# @lc code=end

