#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B: return []
        p1, p2 = 0, 0
        ans = []
        while p1 < len(A) and p2 < len(B):
            if B[p2][0] <= A[p1][1] <= B[p2][1] or A[p1][0] <= B[p2][1] <= A[p1][1]:
                ans.append([max(A[p1][0], B[p2][0]), min(A[p1][1], B[p2][1])])
            if A[p1][1] <= B[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return ans

# @lc code=end

