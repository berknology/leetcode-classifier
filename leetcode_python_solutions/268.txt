class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            ans = ans^i^num
        ans = ans^len(nums)
        return ans
        
