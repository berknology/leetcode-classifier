class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S:
            return 0
        if (S+sum(nums))%2 != 0:
            return 0
        target = (S+sum(nums))//2
        return self.top_down(nums, target, 0, {})
    
    def top_down(self, nums, target, index, memo):
        if index == len(nums):
            if target == 0:
                return 1
            else:
                return 0
        if (target, index) in memo:
            return memo[(target, index)]
        include = self.top_down(nums, target-nums[index], index+1, memo)
        not_include = self.top_down(nums, target, index+1, memo)
        ans = include + not_include
        memo[(target, index)] = ans
        return ans
        

        
"""
P-N = S
P+N = sum
P = (s+sum)//2



"""
