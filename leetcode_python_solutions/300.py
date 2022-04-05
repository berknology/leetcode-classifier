class Solution:
    """
    Longest Increasing Subsequence

    dp[i] denotes the length of the LIS ends with nums[i]

    dp[i] = max(dp[i], 1 + dp[j]) for j < i if dp[i] > dp[j]


    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)


# import bisect
#
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # dp[i] is the smallest ending number of the LISs with length i+1
#         dp = []
#         for num in nums:
#             index = bisect.bisect_left(dp, num)
#             if index == len(dp):
#                 dp.append(num)
#             else:
#                 dp[index] = num
#         return len(dp)
