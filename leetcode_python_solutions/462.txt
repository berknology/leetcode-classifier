import random
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        median = self.quick_select(nums, 0, n-1, n//2)
        ans = 0
        for num in nums:
            ans += abs(median-num)
        return ans
    def quick_select(self, nums, i, j, k):
        pivot_idx = self.partition(nums, i, j)
        if pivot_idx == k:
            return nums[pivot_idx]
        elif pivot_idx < k:
            return self.quick_select(nums, pivot_idx+1, j, k)
        else:
            return self.quick_select(nums, i, pivot_idx-1, k)
    
    def partition(self, nums, i, j):
        random_idx = random.randint(i, j)
        pivot = nums[random_idx]
        nums[random_idx], nums[j] = nums[j], nums[random_idx]
        pivot_idx = i
        for index in range(i, j):
            if nums[index] <= pivot:
                nums[index], nums[pivot_idx] = nums[pivot_idx], nums[index]
                pivot_idx += 1
        nums[pivot_idx], nums[j] = nums[j], nums[pivot_idx]
        return pivot_idx
