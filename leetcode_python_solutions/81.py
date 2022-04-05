class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            while nums[left]==nums[mid]==nums[right] and left < right:
                left += 1
                right -= 1
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        return nums[left] == target
        

"""
binary search
O(log(n))


[2,5,6,0,1,2]
left    0   3   3
right   5   5   3
mid     2   4   


[1,1,1,1,1,0,1,1]
left    0   2   4   5
right   7   5   5   5
mid     3   3   4


"""
