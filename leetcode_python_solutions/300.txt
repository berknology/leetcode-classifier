class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)

"""
Longest Increasing Subsequence

dp[i] denotes the length of the LIS from nums[0:i+1]

dp[i] = max(1 + dp[j]) for j < i if dp[i] > dp[j]
        

"""
