import bisect


class Solution:
    """
    find the length of the longgest common subsequence

    len(target) - length of longgest common subsequence


    convert LCS problem to a LIS problem by using the property that the elements in target is unique

    """

    def minOperations(self, target: List[int], arr: List[int]) -> int:
        m = len(target)
        hash_map = {}
        for i, num in enumerate(target):
            hash_map[num] = i

        nums = [hash_map[e] for e in arr if e in hash_map]

        len_lis = self.lis(nums)

        return m - len_lis

    def lis(self, nums):
        dp = []
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp)
