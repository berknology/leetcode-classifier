#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.backtrack(candidates, target, [], 0)
        return self.ans
    
    def backtrack(self, candidates, target, path, start):
        if target < 0:
            return
        elif target == 0:
            self.ans.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            candidate = candidates[i]
            self.backtrack(candidates, target-candidate, path+[candidate], i+1)

# @lc code=end

# [1, 1, 2, 5, 6, 7, 10]