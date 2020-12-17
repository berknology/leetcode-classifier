#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        hash_table = dict()
        for word in words:
            mask = 0
            for c in word:
                mask = mask | (1 << (ord(c)-ord('a')))
            hash_table[word] = mask
        max_len = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if hash_table[words[i]] & hash_table[words[j]] == 0:
                    max_len = max(max_len, len(words[i])*len(words[j]))
        return max_len

# @lc code=end

