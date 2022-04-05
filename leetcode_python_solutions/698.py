class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        _sum = sum(nums)
        if _sum%k != 0 or _sum//k < max(nums):
            return False
        nums.sort(reverse=True)
        target = [_sum//k]*k
        return self.backtrack(nums, target, 0)
    
    def backtrack(self, nums, target, index):
        if index == len(nums):
            return True
        for i in range(len(target)):
            if target[i] >= nums[index]:
                target[i] -= nums[index]
                if self.backtrack(nums, target, index+1):
                    return True
                target[i] += nums[index]
        return False
        
        
"""
Backtracking


"""
