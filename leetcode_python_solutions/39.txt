class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(candidates, target, path=[], index=0)
        return self.ans
    
    def backtrack(self, candidates, target, path, index):
        if target < 0:
            return
        if target == 0:
            self.ans.append(path)
            return
        for i in range(index, len(candidates)):
            self.backtrack(candidates, target-candidates[i], path+[candidates[i]], i)
        

