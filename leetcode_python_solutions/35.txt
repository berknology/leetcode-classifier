class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid
        return left
        
