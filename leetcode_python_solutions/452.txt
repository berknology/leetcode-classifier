class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: (x[1], x[0]))
        ans = 0
        end = float('-inf')
        for point in points:
            if end >= point[0]:
                end = min(end, point[1])
            else:
                end = point[1]
                ans += 1
        return ans
