class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = self.build_graph(paths)
        ans = [0]*N
        for i in range(N):
            used_colors = set()
            for neighbor in graph[i]:
                used_colors.add(ans[neighbor]) 
            for color in range(1, 5):
                if color not in used_colors:
                    ans[i] = color
                    break
        return ans
    
    def build_graph(self, paths):
        graph = collections.defaultdict(set)
        for path in paths:
            graph[path[0]-1].add(path[1]-1)
            graph[path[1]-1].add(path[0]-1)
        return graph
    
