#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return s
        s = s[::-1]
        word_list = s.split()
        for i, word in enumerate(word_list):
            word_list[i] = word[::-1]
        return ' '.join(word_list)

# @lc code=end

