class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            elif c in '()':
                stack.append(i)
        invalid = set(stack)
        ans = []
        for i, c in enumerate(s):
            if i not in invalid:
                ans.append(c)
        return ''.join(ans)
