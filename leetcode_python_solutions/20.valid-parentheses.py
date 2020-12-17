#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in hash_table:
                stack.append(c)
            else:
                if stack and stack[-1] == hash_table[c]:
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0

# @lc code=end

