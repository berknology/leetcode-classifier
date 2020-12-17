#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ans = []
        self.backtrack(S, [], 0)
        return self.ans

    def backtrack(self, S, path, start):
        if len(path) == len(S):
            self.ans.append(''.join(path))
            return
        for i in range(start, len(S)):
            if S[i].isalpha():
                self.backtrack(S, path+[S[i].lower()], i+1)
                self.backtrack(S, path+[S[i].upper()], i+1)
            else:
                self.backtrack(S, path+[S[i]], i+1)

# @lc code=end

