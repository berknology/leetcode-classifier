class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        min_heap = [(0, (0, 0))]
        seen = set()
        while len(seen) < n:
            w, (u, v) = heapq.heappop(min_heap)
            if v not in seen:
                ans += w
                seen.add(v)
                for j in range(n):
                    if j not in seen and j != v:
                        heapq.heappush(min_heap, (self.distance(points[v], points[j]), (v, j)))
        return ans

    def distance(self, u, v):
        return abs(u[0] - v[0]) + abs(u[1] - v[1])