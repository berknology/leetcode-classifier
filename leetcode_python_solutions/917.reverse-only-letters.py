#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S: return S
        left, right = 0, len(S)-1
        new_s = list(S)
        while left < right:
            if S[left].isalpha() and S[right].isalpha():
                new_s[left], new_s[right] = new_s[right], new_s[left]
                left += 1
                right -= 1
            elif S[left].isalpha():
                right -= 1
            else:
                left += 1
        return ''.join(new_s)
        
# @lc code=end

