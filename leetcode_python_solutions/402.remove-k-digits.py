#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'
        stack = []
        for c in num:
            while k > 0 and stack and c < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(c)
        while k > 0:
            stack.pop()
            k -= 1
        
        string = ''.join(stack)
        if int(string) == 0: 
            return '0'
        else:
            return string.lstrip('0')

# @lc code=end

