#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        cur_interval = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if cur_interval[1] >= intervals[i][0]:
                cur_interval = [min(cur_interval[0], intervals[i][0]), max(cur_interval[1], intervals[i][1])]
            else:
                ans.append(cur_interval)
                cur_interval = intervals[i]
        ans.append(cur_interval)
        return ans         

# @lc code=end

