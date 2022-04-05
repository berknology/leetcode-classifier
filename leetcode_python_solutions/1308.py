class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        list_s = list(s)
        graph = self.build_graph(pairs)
        visited = [False]*len(s)
        for i in range(len(s)):
            if not visited[i]:
                comp = []
                self.dfs(graph, i, visited, comp)
                letters = [s[j] for j in comp]
                comp.sort()
                letters.sort()
                for j in range(len(comp)):
                    list_s[comp[j]] = letters[j]
        return ''.join(list_s)
    
    def build_graph(self, pairs):
        graph = collections.defaultdict(list)
        for pair in pairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        return graph
    
    def dfs(self, graph, i, visited, comp):
        comp.append(i)
        visited[i] = True
        for nei in graph[i]:
            if not visited[nei]:
                self.dfs(graph, nei, visited, comp)
        
