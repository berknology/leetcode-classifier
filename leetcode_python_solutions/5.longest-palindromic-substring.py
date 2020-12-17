#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        self.max_len = 0
        self.ans = ''
        for i in range(len(s)):
            self.expand(s, i, i)
            self.expand(s, i-1, i)
        return self.ans
    
    def expand(self, s, i, j):
        length = 0
        while 0 <= i < len(s) and 0 <= j < len(s):
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break
        length = j-i-1
        if length > self.max_len:
            self.max_len = length
            self.ans = s[i+1:j]
    
# @lc code=end

