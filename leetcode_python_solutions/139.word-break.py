#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        capacity = len(s)
        dp = [False]*(capacity+1)
        dp[0] = True
        for i in range(1, capacity+1):
            for j in range(i):
                sub_str = s[j:i]
                if sub_str in word_set:
                    dp[i] = dp[i] or dp[j]
        return dp[-1]

# @lc code=end

