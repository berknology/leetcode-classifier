#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes: return True
        graph = self.build_graph(dislikes)
        visited = [0]*N
        for i in range(N):
            if visited[i] == 0:
                if not self.dfs(graph, i, visited, 1):
                    return False
        return True

    def build_graph(self, dislikes):
        graph = collections.defaultdict(set)
        for dislike in dislikes:
            graph[dislike[0]-1].add(dislike[1]-1)
            graph[dislike[1]-1].add(dislike[0]-1)
        return graph

    def dfs(self, graph, i, visited, color):
        visited[i] = color
        for nei in graph[i]:
            if visited[nei] != 0:
                if visited[nei] == color:
                    return False
            else:
                if not self.dfs(graph, nei, visited, -color):
                    return False
        return True

# @lc code=end

