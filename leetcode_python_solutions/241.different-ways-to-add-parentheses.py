#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input:
            return []
        if input.isdigit():
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(l+r)
                        elif c == '-':
                            res.append(l-r)
                        else:
                            res.append(l*r)
        return res

# @lc code=end

