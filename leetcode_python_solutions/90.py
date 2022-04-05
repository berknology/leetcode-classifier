class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        self.ans = []
        nums.sort()
        self.backtrack(nums, path=[], start=0)
        return self.ans
    def backtrack(self, nums, path, start):
        self.ans.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.backtrack(nums, path+[nums[i]], i+1)
