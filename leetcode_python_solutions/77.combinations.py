#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(n, k, [], 1)
        return self.ans
    
    def backtrack(self, n, k, path, start):
        if len(path) == k:
            self.ans.append(path)
            return
        for i in range(start, n+1):
            self.backtrack(n, k, path+[i], i+1)

# @lc code=end

