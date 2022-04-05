class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

"""
[3,4,5,1,2]
left    0   3   3    
right   4   4   3
mid     2   3   3

[4,5,6,7,0,1,2]
l   0   4   4   4
r   6   6   5   4
m   3   5   4   

"""
