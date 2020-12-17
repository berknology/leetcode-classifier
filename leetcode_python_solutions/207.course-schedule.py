#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegree = self.build_graph(prerequisites, numCourses)
        ans = []
        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return len(ans) == numCourses

    def build_graph(self, prerequisites, n):
        graph = collections.defaultdict(list)
        indegree = [0]*n
        for req in prerequisites:
            graph[req[1]].append(req[0])
            indegree[req[0]] += 1
        return graph, indegree

# @lc code=end

