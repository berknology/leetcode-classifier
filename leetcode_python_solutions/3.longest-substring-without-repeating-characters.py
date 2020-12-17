#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        start, end = 0, 1
        max_len = 0
        hash_set = set()
        hash_set.add(s[0])
        while end < len(s):
            if s[end] in hash_set:
                hash_set.remove(s[start])
                start += 1
            else:
                hash_set.add(s[end])
                max_len = max(max_len, len(hash_set))
                end += 1
        return max_len
            
# @lc code=end
