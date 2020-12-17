#
# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#

# @lc code=start
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.ans = []
        self.backtrack(S, path=[], index=0)
        return self.ans

    def backtrack(self, S, path, index):
        if index == len(S) and len(path) >= 3:
            self.ans = path
            return
        for i in range(index, len(S)):
            sub_str = S[index:i+1]
            if (len(sub_str) > 1 and sub_str[0] == '0') or int(sub_str) > 2**31-1:
                break
            if len(path) >= 2 and int(sub_str) != path[-1] + path[-2]:
                continue
            self.backtrack(S, path+[int(sub_str)], i+1)

# @lc code=end

