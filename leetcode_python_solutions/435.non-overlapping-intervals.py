#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        ans = 0
        end = float('-inf')
        for interval in intervals:
            if end > interval[0]:
                end = min(end, interval[1])
                ans += 1
            else:
                end = interval[1]
        return ans
# @lc code=end

