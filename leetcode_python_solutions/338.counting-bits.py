#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1, num+1):
            dp[i] = dp[i&(i-1)] + 1
        return dp

"""
0   0000    0
1   0001    1
2   0010    1
3   0011    2
4   0100    1
5   0101    2
6   0110    2
7   0111    3
8   1000    1
9   1001    2
10  1010    2
11  1011    3
"""

# @lc code=end

