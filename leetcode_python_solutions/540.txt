class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if mid%2 != 0:
                mid = mid - 1
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
                
        
        
"""

Binary search

[1,1,2,3,3,4,4,8,8]

[3,3,7,7,10,11,11]

"""
