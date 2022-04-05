class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        stack = []
        for c in num:
            while k > 0 and stack and c < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(c)
        while k > 0:
            stack.pop()
            k -= 1
        ans = ''.join(stack).lstrip('0')
        return ans if ans else '0'
        
"""
monotone increasing stack

stack


"""
