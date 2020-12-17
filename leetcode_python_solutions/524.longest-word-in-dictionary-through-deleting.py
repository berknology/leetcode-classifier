#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans = ''
        for word in d:
            if self.is_feasible(s, word):
                if len(word) > len(ans) or (len(word)==len(ans) and word < ans):
                    ans = word
        return ans

    def is_feasible(self, s, word):
        if not word: return True
        if not s: return False
        p1 = p2 = 0
        while p1 < len(s) and p2 < len(word):
            if s[p1] == word[p2]:
                p2 += 1
            p1 += 1
        return p2 == len(word)

# @lc code=end

