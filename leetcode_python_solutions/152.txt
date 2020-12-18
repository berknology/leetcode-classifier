class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = cur_min = cur_max = nums[0]
        for i in range(1, len(nums)):
            cur_min, cur_max = min(nums[i], nums[i]*cur_min, nums[i]*cur_max), max(nums[i], nums[i]*cur_min, nums[i]*cur_max)
            ans = max(ans, cur_max)
        return ans

        
"""
[2, 3, -2, 4]

Naive solution: O(n^2)


cur_min   2     3   -12    -48

cur_max   2     6   -2      4

"""
