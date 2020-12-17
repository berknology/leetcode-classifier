#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s: return s
        left, right = 0, len(s)-1
        new_s = list(s)
        while left < right:
            if s[left].lower() in 'aeiou' and s[right].lower() in 'aeiou': 
                new_s[left], new_s[right] = new_s[right], new_s[left]
                left += 1
                right -= 1
            elif s[left].lower() in 'aeiou':
                right -= 1
            else:
                left += 1
        return ''.join(new_s)

# @lc code=end

