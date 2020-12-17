#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        if n <= 1: return n
        pairs.sort(key = lambda x: (x[1], x[0]))
        dp = [1]*len(pairs)
        for i in range(n):
            for j in range(i):
                if pairs[j][-1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

# @lc code=end

