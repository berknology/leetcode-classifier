#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        cnt_p = collections.Counter(p)
        cnt_s = collections.Counter(s[0:len_p-1])
        ans = []
        for i in range(len_p-1, len_s):
            cnt_s[s[i]] += 1
            if cnt_s == cnt_p:
                ans.append(i-len_p+1)
            cnt_s[s[i-len_p+1]] -= 1
            if cnt_s[s[i-len_p+1]] == 0:
                del cnt_s[s[i-len_p+1]]
        return ans

# @lc code=end

