#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not queries: return []
        ans = [-1]*len(queries)
        graph = self.build_graph(equations, values)
        for i, query in enumerate(queries):
            ans[i] = self.bfs(graph, query[0], query[1])
        return ans
    
    def build_graph(self, equations, values):
        graph = collections.defaultdict(set)
        for i, equ in enumerate(equations):
            graph[equ[0]].add((equ[1], values[i]))
            graph[equ[1]].add((equ[0], 1.0/values[i]))
        return graph

    def bfs(self, graph, start, end):
        if end not in graph: return -1
        if start == end: return 1
        visited = set()
        queue = collections.deque([(start, 1)])
        while queue:
            node, prod = queue.popleft()
            if node == end: return prod 
            for nei in graph[node]:
                if nei[0] not in visited:
                    visited.add(nei[0])
                    queue.append((nei[0], prod*nei[1]))
        return -1

# @lc code=end

