#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        visited = [False]*len(nums)
        self.backtrack(nums, visited, [])
        return self.ans

    def backtrack(self, nums, visited, path):
        if len(path) == len(nums):
            self.ans.append(path)
            return
        for i, num in enumerate(nums):
            if not visited[i]:
                if i > 0 and not visited[i-1] and nums[i] == nums[i-1]:
                    continue
                visited[i] = True
                self.backtrack(nums, visited, path+[num])
                visited[i] = False

# @lc code=end

