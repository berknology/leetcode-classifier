#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        new_s = list(s)
        n = len(s)
        visited = [False]*n
        graph = self.build_graph(pairs)
        for i in range(n):
            if not visited[i]:
                components = []
                self.dfs(graph, visited, s, i, components)
                chars = [s[index] for index in components]
                chars.sort()
                components.sort()
                for i, index in enumerate(components):
                    new_s[index] = chars[i]
        return ''.join(new_s)

    def build_graph(self, pairs):
        graph = collections.defaultdict(list)
        for pair in pairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        return graph
    
    def dfs(self, graph, visited, s, i, components):
        visited[i] = True
        components.append(i)
        for j in graph[i]:
            if not visited[j]:
                self.dfs(graph, visited, s, j, components)

# @lc code=end

