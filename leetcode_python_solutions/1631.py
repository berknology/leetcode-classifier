class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        effort = [[float("inf")]*n for _ in range(m)]
        effort[0][0] = 0
        min_heap = []
        heapq.heappush(min_heap, (0, 0, 0))
        while min_heap:
            dis, i, j = heapq.heappop(min_heap)
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n:
                    e = max(effort[i][j], abs(heights[i][j]-heights[x][y]))
                    if effort[x][y] > e:
                        effort[x][y] = e
                        heapq.heappush(min_heap, (effort[x][y], x, y))
        return effort[-1][-1]