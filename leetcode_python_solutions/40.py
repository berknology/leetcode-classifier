class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.backtrack(candidates, target, path=[], index=0)
        return self.ans
    
    def backtrack(self, candidates, target, path, index):
        if target < 0:
            return
        elif target == 0:
            self.ans.append(path)
            return
        else:
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                candidate = candidates[i]
                self.backtrack(candidates, target-candidate, path+[candidate], i+1)

                

"""
[1, 1, 2, 5, 6, 7, 10]

"""
