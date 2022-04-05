class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return
        cur_sum = 0
        max_sum = float('-inf')
        for num in nums:
            cur_sum = max(num+cur_sum, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
        
