class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegree = self.build_graph(numCourses, prerequisites)
        queue = collections.deque([i for i in range(len(indegree)) if indegree[i] == 0])
        while queue:
            node = queue.pop()
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return sum(indegree) == 0
        
    def build_graph(self, numCourses, prerequisites):
        indegree = [0]*numCourses
        graph = collections.defaultdict(list)
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        return graph, indegree
        
"""
DAG
Topological sort
indegree

"""
