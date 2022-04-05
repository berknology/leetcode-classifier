class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        return self.backtrack(nums, target, {})
    
    def backtrack(self, nums, target, memo):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if target in memo:
            return memo[target]
        ans = 0
        for i in range(len(nums)):
            ans += self.backtrack(nums, target-nums[i], memo)
        memo[target] = ans
        return ans
        
        
"""
backtracking
exhaustive search 


"""
