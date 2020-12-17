#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        self.ans = []
        self.backtrack(nums, [], 0)
        return self.ans
    
    def backtrack(self, nums, path, start):
        self.ans.append(path)
        for i in range(start, len(nums)):
            self.backtrack(nums, path+[nums[i]], i+1)



# @lc code=end

