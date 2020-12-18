class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum %2 != 0:
            return False
        target = _sum//2
        return self.top_down(nums, target, 0, {})
    
    def top_down(self, nums, target, index, memo):
        if target < 0 or index >= len(nums):
            return False
        if target == 0:
            return True
        if (index, target) in memo:
            return memo[(index, target)]
        include = self.top_down(nums, target-nums[index], index+1, memo)
        not_include = self.top_down(nums, target, index+1, memo)
        memo[(index, target)] = include or not_include
        return memo[(index, target)]
        
        
        
"""
backtracking

knapsack problem



"""
