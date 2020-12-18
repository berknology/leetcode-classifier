class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        start = 0
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i+1
                else:
                    stack.pop()
                    if stack:
                        res = max(res, i - stack[-1])
                    else:
                        res = max(res, i - start + 1)
        return res

"""
use stack


()()

"""
