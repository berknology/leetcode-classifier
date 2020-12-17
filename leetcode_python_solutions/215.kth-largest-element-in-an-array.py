#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.quick_select(nums, 0, n-1, n-k)
    
    def quick_select(self, nums, i, j, k):
        pivot_idx = self.partition(nums, i, j)
        if pivot_idx == k:
            return nums[pivot_idx]
        elif pivot_idx < k:
            return self.quick_select(nums, pivot_idx+1, j, k)
        else:
            return self.quick_select(nums, i, pivot_idx-1, k)

    def partition(self, nums, i, j):
        rand_idx = random.randint(i, j)
        pivot = nums[rand_idx]
        nums[rand_idx], nums[j] = nums[j], nums[rand_idx]
        pivot_idx = i
        for index in range(i, j):
            if nums[index] <= pivot:
                nums[index], nums[pivot_idx] = nums[pivot_idx], nums[index]
                pivot_idx += 1
        nums[pivot_idx], nums[j] = nums[j], nums[pivot_idx]
        return pivot_idx
        
# @lc code=end

