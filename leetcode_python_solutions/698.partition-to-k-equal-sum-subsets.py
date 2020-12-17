#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum = sum(nums)
        if _sum%k != 0 or max(nums)*k > _sum: 
            return False
        targets = [_sum//k]*k
        nums.sort(reverse=True)
        return self.backtrack(nums, targets, 0)
    
    def backtrack(self, nums, targets, index):
        if index == len(nums):
            return True
        for i in range(len(targets)):
            if targets[i] >= nums[index]:
                targets[i] -= nums[index]
                if self.backtrack(nums, targets, index+1):
                    return True
                targets[i] += nums[index]
        return False


# @lc code=end

