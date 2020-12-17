#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)): 
            cost[i] += min(cost[i - 1],cost[i - 2])
        return min(cost[-1], cost[-2])


# dp[i] = cost[i]+min(dp[i-2], dp[i-1])

# @lc code=end

