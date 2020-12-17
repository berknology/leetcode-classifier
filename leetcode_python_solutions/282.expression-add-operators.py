#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.ans = []
        self.backtrack(num, target, '', 0, 0, 0)
        return self.ans

    def backtrack(self, num, target, path, index, val, pre):
        if index == len(num) and val == target:
            self.ans.append(path)
            return
        for i in range(index, len(num)):
            sub_str = num[index:i+1]
            if len(sub_str) > 1 and sub_str[0] == '0':
                break
            if len(path) == 0:
                self.backtrack(num, target, sub_str, i+1, val+int(sub_str), int(sub_str))
            else:
                self.backtrack(num, target, path+'+'+sub_str, i+1, val+int(sub_str), +int(sub_str))
                self.backtrack(num, target, path+'-'+sub_str, i+1, val-int(sub_str), -int(sub_str))
                self.backtrack(num, target, path+'*'+sub_str, i+1, val-pre+pre*int(sub_str), pre*int(sub_str))

# @lc code=end

