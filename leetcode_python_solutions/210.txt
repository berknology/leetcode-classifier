class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, ind = self.build_graph(prerequisites)
        ans = self.top_sort(graph, ind, numCourses)
        return ans if len(ans) == numCourses else []
    def build_graph(self, prerequisites):
        graph = collections.defaultdict(list)
        ind = collections.defaultdict(int)
        for req in prerequisites:
            graph[req[1]].append(req[0])
            ind[req[0]] += 1
        return graph, ind
    def top_sort(self, graph, ind, n):
        ans = []
        queue = collections.deque([i for i in range(n) if ind[i]==0])
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in graph[node]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    queue.append(nei)
        return ans
