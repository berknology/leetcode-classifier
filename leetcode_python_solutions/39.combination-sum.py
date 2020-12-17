#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            candidate = candidates[i]
            self.backtrack(candidates, target-candidate, path+[candidate], i)

# @lc code=end

