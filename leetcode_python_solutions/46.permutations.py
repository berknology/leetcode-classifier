#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False]*len(nums)
        ans = []
        self.backtrack(nums, visited, [], ans)
        return ans

    def backtrack(self, nums, visited, path, ans):
        if len(path) == len(nums):
            ans.append(path)
            return
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                self.backtrack(nums, visited, path+[nums[i]], ans)
                visited[i] = False

# @lc code=end

