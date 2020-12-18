class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        _sum = sum(nums)
        if _sum%4 != 0 or max(nums) > _sum//4:
            return False
        target = [_sum//4]*4
        nums.sort(reverse = True)
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
4x = sum(nums)

split elements into 4 parts with equal sum

"""
