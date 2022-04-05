class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0]*n
        for i in range(n):
            if visited[i] == 0:
                if not self.dfs(graph, i, visited, 1):
                    return False
        return True
    
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
        
