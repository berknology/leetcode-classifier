class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1]
        return self.top_down(nums, 0, len(nums)-1, memo={})
    
    def top_down(self, nums, i, j, memo):
        if i+1 == j: 
            return 0
        if (i, j) not in memo:
            ans = 0
            for k in range(i+1, j):
                ans = max(ans, nums[i]*nums[j]*nums[k]+self.top_down(nums, i, k, memo)+self.top_down(nums, k, j, memo))
            memo[(i, j)] = ans
        return memo[(i, j)]

        
"""
[3,1,5,8]

Naive solution is recursion

[1,5,8]    [3,5,8]     [3,1,8]     [3,1,5]

DP



"""
