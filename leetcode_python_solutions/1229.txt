class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        ans = [float('inf')]*n
        blue_graph = self.build_graph(blue_edges)
        red_graph = self.build_graph(red_edges)
        queue = collections.deque([(0, 0, 1), (0, 0, -1)])
        while queue:
            node, step, color = queue.popleft()
            ans[node] = min(ans[node], step)
            if color == 1:
                graph = blue_graph
            else:
                graph = red_graph
            for nei in list(graph[node]):
                queue.append((nei, step+1, -color))
                graph[node].remove(nei)
        return [e if e != float('inf') else -1 for e in ans]

    def build_graph(self, edges):
        graph = collections.defaultdict(set)
        for e in edges:
            graph[e[0]].add(e[1])
        return graph
    
