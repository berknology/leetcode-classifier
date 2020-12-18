class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        visited = [False]*len(nums)
        self.backtrack(nums, visited, path=[])
        return self.ans
    
    def backtrack(self, nums, visited, path=[]):
        if len(path) == len(nums):
            self.ans.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            if not visited[i]:
                visited[i] = True
                self.backtrack(nums, visited, path+[nums[i]])
                visited[i] = False

                
"""
[1, 1, 2]



"""
