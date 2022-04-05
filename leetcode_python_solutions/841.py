class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        graph = self.build_graph(rooms)
        self.dfs(graph, visited, 0)
        return sum(visited) == n
    def build_graph(self, rooms):
        graph = collections.defaultdict(list)
        for i, room in enumerate(rooms):
            graph[i].extend(room)
        return graph
    def dfs(self, graph, visited, index):
        visited[index] = True
        for nei in graph[index]:
            if nei != index and not visited[nei]:
                self.dfs(graph, visited, nei)
