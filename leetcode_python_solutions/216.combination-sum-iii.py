#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(k, n, [], 1)
        return self.ans

    def backtrack(self, k, n, path, start):
        if len(path) == k and n == 0:
            self.ans.append(path)
            return
        for i in range(start, 10):
            self.backtrack(k, n-i, path+[i], i+1)


# @lc code=end

