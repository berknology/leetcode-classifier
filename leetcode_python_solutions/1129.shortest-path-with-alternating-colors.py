#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#

# @lc code=start
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        blue = 1
        red = -1
        ans = [float('inf')]*n
        red_graph = self.build_graph(red_edges)
        blue_graph = self.build_graph(blue_edges)
        queue = collections.deque([(0, 0, blue), (0, 0, red)])
        while queue:
            node, step, color = queue.popleft()
            ans[node] = min(ans[node], step)
            graph = blue_graph if color == blue else red_graph
            for nei in list(graph[node]):
                graph[node].remove(nei)
                queue.append((nei, step+1, -color))
        return [item if item != float('inf') else -1 for item in ans]

    def build_graph(self, edges):
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
        return graph

# @lc code=end

