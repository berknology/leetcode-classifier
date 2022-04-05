class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        gra, out = self.build_graph(graph)
        ans = self.top_sort(gra, out, len(graph))
        return [i for i in range(len(graph)) if i in ans]
    def build_graph(self, graph):
        gra = collections.defaultdict(list)
        out = collections.defaultdict(int)
        for i in range(len(graph)):
            for nei in graph[i]:
                gra[nei].append(i)
                out[i] += 1
        return gra, out
    def top_sort(self, gra, out, n):
        ans = set()
        queue = collections.deque([i for i in range(n) if out[i]==0])
        while queue:
            node = queue.popleft()
            ans.add(node)
            for nei in gra[node]:
                out[nei] -= 1
                if out[nei] == 0:
                    queue.append(nei)
        return ans
