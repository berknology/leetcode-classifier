#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = collections.Counter(s)
        ans = 0
        has_single_char = False
        for c in cnt:
            if cnt[c]%2 == 0:
                ans += cnt[c]
            else:
                ans += max(0, cnt[c]-1)
                has_single_char = True
        return ans + has_single_char

# @lc code=end

